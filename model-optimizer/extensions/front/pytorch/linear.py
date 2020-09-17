"""
 Copyright (C) 2018-2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import numpy as np

from mo.front.common.replacement import FrontReplacementOp
from mo.graph.graph import Graph, Node
from mo.ops.const import Const
from extensions.ops.MatMul import MatMul
from mo.ops.reshape import Reshape


class ComplexAbs(FrontReplacementOp):
    op = 'Linear'
    enabled = True

    def replace_op(self, graph: Graph, node: Node):
        shape = Const(graph, {'value': [0, -1]}).create_node()
        flatten = Reshape(graph, dict(name=node.in_node(0).name + '/flatten')).create_node([node.in_node(0), shape])

        inputs = [flatten, node.in_node(1)]
        if len(node.in_nodes()) > 2:
            inputs.append(node.in_node(2))  # bias
        matmul = MatMul(graph, dict(name=node.name, transpose_b=True)).create_node(inputs)
        return [matmul.id]
