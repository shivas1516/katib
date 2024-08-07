# Copyright 2022 The Kubeflow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from keras import backend as K
from keras.layers import Activation
from keras.layers import AveragePooling2D
from keras.layers import BatchNormalization
from keras.layers import concatenate
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import GlobalAveragePooling2D
from keras.layers import Input
from keras.layers import MaxPooling2D
from keras.layers import ZeroPadding2D
from keras.models import Model
import numpy as np
from op_library import concat
from op_library import conv
from op_library import dw_conv
from op_library import reduction
from op_library import sp_conv


class ModelConstructor(object):
    def __init__(self, arc_json, nn_json):
        self.arch = json.loads(arc_json)
        nn_config = json.loads(nn_json)
        self.num_layers = nn_config['num_layers']
        self.input_sizes = nn_config['input_sizes']
        self.output_size = nn_config['output_sizes'][-1]
        self.embedding = nn_config['embedding']

    def build_model(self):
        # a list of the data all layers
        all_layers = [0 for _ in range(self.num_layers + 1)]
        # a list of all the dimensions of all layers
        all_dims = [0 for _ in range(self.num_layers + 1)]

        # ================= Stacking layers =================
        # Input Layer. Layer 0
        input_layer = Input(shape=self.input_sizes)
        all_layers[0] = input_layer

        # Intermediate Layers. Starting from layer 1.
        for l in range(1, self.num_layers + 1):
            input_layers = list()
            opt = self.arch[l - 1][0]
            opt_config = self.embedding[str(opt)]
            skip = self.arch[l - 1][1:l+1]

            # set up the connection to the previous layer first
            input_layers.append(all_layers[l - 1])

            # then add skip connections
            for i in range(l - 1):
                if l > 1 and skip[i] == 1:
                    input_layers.append(all_layers[i])

            layer_input = concat(input_layers)
            if opt_config['opt_type'] == 'convolution':
                layer_output = conv(layer_input, opt_config)
            if opt_config['opt_type'] == 'separable_convolution':
                layer_output = sp_conv(layer_input, opt_config)
            if opt_config['opt_type'] == 'depthwise_convolution':
                layer_output = dw_conv(layer_input, opt_config)
            elif opt_config['opt_type'] == 'reduction':
                layer_output = reduction(layer_input, opt_config)

            all_layers[l] = layer_output

        # Final Layer
        # Global Average Pooling, then Fully connected with softmax.
        avgpooled = GlobalAveragePooling2D()(all_layers[self.num_layers])
        dropped = Dropout(0.4)(avgpooled)
        logits = Dense(units=self.output_size,
                       activation='softmax')(dropped)

        # Encapsulate the model
        self.model = Model(inputs=input_layer, outputs=logits)

        return self.model
