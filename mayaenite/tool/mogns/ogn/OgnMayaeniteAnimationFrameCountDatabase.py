"""Support for simplified access to data on nodes of type MayaeniteToolMognsExtension.MayaeniteAnimationFrameCount

Returns The Frame Count Of The Input Prim
"""

import sys
import traceback
import usdrt

import omni.graph.core as og
import omni.graph.core._omni_graph_core as _og
import omni.graph.tools.ogn as ogn



class OgnMayaeniteAnimationFrameCountDatabase(og.Database):
    """Helper class providing simplified access to data on nodes of type MayaeniteToolMognsExtension.MayaeniteAnimationFrameCount

    Class Members:
        node: Node being evaluated

    Attribute Value Properties:
        Inputs:
            inputs.frameRate
            inputs.prim
            inputs.useSceneFrameRate
        Outputs:
            outputs.frameCount
            outputs.outPrim
    """

    # Imprint the generator and target ABI versions in the file for JIT generation
    GENERATOR_VERSION = (1, 41, 3)
    TARGET_VERSION = (2, 139, 12)

    # This is an internal object that provides per-class storage of a per-node data dictionary
    PER_NODE_DATA = {}

    # This is an internal object that describes unchanging attributes in a generic way
    # The values in this list are in no particular order, as a per-attribute tuple
    #     Name, Type, ExtendedTypeIndex, UiName, Description, Metadata,
    #     Is_Required, DefaultValue, Is_Deprecated, DeprecationMsg
    # You should not need to access any of this data directly, use the defined database interfaces
    INTERFACE = og.Database._get_interface([
        ('inputs:frameRate', 'timecode', 0, 'Frame Rate', 'The Frame Rate The Animation Was Generated At', {ogn.MetadataKeys.DEFAULT: '24.0'}, True, 24.0, False, ''),
        ('inputs:prim', 'target', 0, 'Prim', 'The Prim To Get The Frame Count For', {ogn.MetadataKeys.DEFAULT: '0'}, True, [], False, ''),
        ('inputs:useSceneFrameRate', 'bool', 0, 'Use Scene Frame Rate', 'When checked this node will use the frame rate of the root layer', {ogn.MetadataKeys.DEFAULT: 'false'}, True, False, False, ''),
        ('outputs:frameCount', 'int', 0, 'Frame Count', 'The Amount Of Frames The Input Prim Has', {}, True, None, False, ''),
        ('outputs:outPrim', 'target', 0, 'Prim', 'outputs the input path for exe flow into down streem inputs', {ogn.MetadataKeys.DEFAULT: 'null'}, True, [], False, ''),
    ])

    @classmethod
    def _populate_role_data(cls):
        """Populate a role structure with the non-default roles on this node type"""
        role_data = super()._populate_role_data()
        role_data.inputs.frameRate = og.AttributeRole.TIMECODE
        role_data.inputs.prim = og.AttributeRole.TARGET
        role_data.outputs.outPrim = og.AttributeRole.TARGET
        return role_data

    class ValuesForInputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {"frameRate", "useSceneFrameRate", "_setting_locked", "_batchedReadAttributes", "_batchedReadValues"}
        """Helper class that creates natural hierarchical access to input attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self._batchedReadAttributes = [self._attributes.frameRate, self._attributes.useSceneFrameRate]
            self._batchedReadValues = [24.0, False]

        @property
        def prim(self):
            data_view = og.AttributeValueHelper(self._attributes.prim)
            return data_view.get()

        @prim.setter
        def prim(self, value):
            if self._setting_locked:
                raise og.ReadOnlyError(self._attributes.prim)
            data_view = og.AttributeValueHelper(self._attributes.prim)
            data_view.set(value)
            self.prim_size = data_view.get_array_size()

        @property
        def frameRate(self):
            return self._batchedReadValues[0]

        @frameRate.setter
        def frameRate(self, value):
            self._batchedReadValues[0] = value

        @property
        def useSceneFrameRate(self):
            return self._batchedReadValues[1]

        @useSceneFrameRate.setter
        def useSceneFrameRate(self, value):
            self._batchedReadValues[1] = value

        def __getattr__(self, item: str):
            if item in self.LOCAL_PROPERTY_NAMES:
                return object.__getattribute__(self, item)
            else:
                return super().__getattr__(item)

        def __setattr__(self, item: str, new_value):
            if item in self.LOCAL_PROPERTY_NAMES:
                object.__setattr__(self, item, new_value)
            else:
                super().__setattr__(item, new_value)

        def _prefetch(self):
            readAttributes = self._batchedReadAttributes
            newValues = _og._prefetch_input_attributes_data(readAttributes)
            if len(readAttributes) == len(newValues):
                self._batchedReadValues = newValues

    class ValuesForOutputs(og.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES = {"frameCount", "_batchedWriteValues"}
        """Helper class that creates natural hierarchical access to output attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)
            self.outPrim_size = None
            self._batchedWriteValues = { }

        @property
        def outPrim(self):
            data_view = og.AttributeValueHelper(self._attributes.outPrim)
            return data_view.get(reserved_element_count=self.outPrim_size)

        @outPrim.setter
        def outPrim(self, value):
            data_view = og.AttributeValueHelper(self._attributes.outPrim)
            data_view.set(value)
            self.outPrim_size = data_view.get_array_size()

        @property
        def frameCount(self):
            value = self._batchedWriteValues.get(self._attributes.frameCount)
            if value:
                return value
            else:
                data_view = og.AttributeValueHelper(self._attributes.frameCount)
                return data_view.get()

        @frameCount.setter
        def frameCount(self, value):
            self._batchedWriteValues[self._attributes.frameCount] = value

        def __getattr__(self, item: str):
            if item in self.LOCAL_PROPERTY_NAMES:
                return object.__getattribute__(self, item)
            else:
                return super().__getattr__(item)

        def __setattr__(self, item: str, new_value):
            if item in self.LOCAL_PROPERTY_NAMES:
                object.__setattr__(self, item, new_value)
            else:
                super().__setattr__(item, new_value)

        def _commit(self):
            _og._commit_output_attributes_data(self._batchedWriteValues)
            self._batchedWriteValues = { }

    class ValuesForState(og.DynamicAttributeAccess):
        """Helper class that creates natural hierarchical access to state attributes"""
        def __init__(self, node: og.Node, attributes, dynamic_attributes: og.DynamicAttributeInterface):
            """Initialize simplified access for the attribute data"""
            context = node.get_graph().get_default_graph_context()
            super().__init__(context, node, attributes, dynamic_attributes)

    def __init__(self, node):
        super().__init__(node)
        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_INPUT)
        self.inputs = OgnMayaeniteAnimationFrameCountDatabase.ValuesForInputs(node, self.attributes.inputs, dynamic_attributes)
        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_OUTPUT)
        self.outputs = OgnMayaeniteAnimationFrameCountDatabase.ValuesForOutputs(node, self.attributes.outputs, dynamic_attributes)
        dynamic_attributes = self.dynamic_attribute_data(node, og.AttributePortType.ATTRIBUTE_PORT_TYPE_STATE)
        self.state = OgnMayaeniteAnimationFrameCountDatabase.ValuesForState(node, self.attributes.state, dynamic_attributes)

    class abi:
        """Class defining the ABI interface for the node type"""

        @staticmethod
        def get_node_type():
            get_node_type_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'get_node_type', None)
            if callable(get_node_type_function):
                return get_node_type_function()
            return 'MayaeniteToolMognsExtension.MayaeniteAnimationFrameCount'

        @staticmethod
        def compute(context, node):
            def database_valid():
                return True
            try:
                per_node_data = OgnMayaeniteAnimationFrameCountDatabase.PER_NODE_DATA[node.node_id()]
                db = per_node_data.get('_db')
                if db is None:
                    db = OgnMayaeniteAnimationFrameCountDatabase(node)
                    per_node_data['_db'] = db
                if not database_valid():
                    per_node_data['_db'] = None
                    return False
            except:
                db = OgnMayaeniteAnimationFrameCountDatabase(node)

            try:
                compute_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'compute', None)
                if callable(compute_function) and compute_function.__code__.co_argcount > 1:
                    return compute_function(context, node)

                db.inputs._prefetch()
                db.inputs._setting_locked = True
                with og.in_compute():
                    return OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS.compute(db)
            except Exception as error:
                stack_trace = "".join(traceback.format_tb(sys.exc_info()[2].tb_next))
                db.log_error(f'Assertion raised in compute - {error}\n{stack_trace}', add_context=False)
            finally:
                db.inputs._setting_locked = False
                db.outputs._commit()
            return False

        @staticmethod
        def initialize(context, node):
            OgnMayaeniteAnimationFrameCountDatabase._initialize_per_node_data(node)
            initialize_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'initialize', None)
            if callable(initialize_function):
                initialize_function(context, node)

            per_node_data = OgnMayaeniteAnimationFrameCountDatabase.PER_NODE_DATA[node.node_id()]
            def on_connection_or_disconnection(*args):
                per_node_data['_db'] = None

            node.register_on_connected_callback(on_connection_or_disconnection)
            node.register_on_disconnected_callback(on_connection_or_disconnection)

        @staticmethod
        def release(node):
            release_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'release', None)
            if callable(release_function):
                release_function(node)
            OgnMayaeniteAnimationFrameCountDatabase._release_per_node_data(node)

        @staticmethod
        def release_instance(node, target):
            OgnMayaeniteAnimationFrameCountDatabase._release_per_node_instance_data(node, target)

        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            update_node_version_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'update_node_version', None)
            if callable(update_node_version_function):
                return update_node_version_function(context, node, old_version, new_version)
            return False

        @staticmethod
        def initialize_type(node_type):
            initialize_type_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'initialize_type', None)
            needs_initializing = True
            if callable(initialize_type_function):
                needs_initializing = initialize_type_function(node_type)
            if needs_initializing:
                node_type.set_metadata(ogn.MetadataKeys.EXTENSION, "mayaenite.tool.mogns")
                node_type.set_metadata(ogn.MetadataKeys.UI_NAME, "Mayaenite Animation Frame Count")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORIES, "Mayaenite")
                node_type.set_metadata(ogn.MetadataKeys.CATEGORY_DESCRIPTIONS, "Mayaenite,Nodes implementing lights for rendering")
                node_type.set_metadata(ogn.MetadataKeys.DESCRIPTION, "Returns The Frame Count Of The Input Prim")
                node_type.set_metadata(ogn.MetadataKeys.LANGUAGE, "Python")
                OgnMayaeniteAnimationFrameCountDatabase.INTERFACE.add_to_node_type(node_type)

        @staticmethod
        def on_connection_type_resolve(node):
            on_connection_type_resolve_function = getattr(OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS, 'on_connection_type_resolve', None)
            if callable(on_connection_type_resolve_function):
                on_connection_type_resolve_function(node)

    NODE_TYPE_CLASS = None

    @staticmethod
    def register(node_type_class):
        OgnMayaeniteAnimationFrameCountDatabase.NODE_TYPE_CLASS = node_type_class
        og.register_node_type(OgnMayaeniteAnimationFrameCountDatabase.abi, 1)

    @staticmethod
    def deregister():
        og.deregister_node_type("MayaeniteToolMognsExtension.MayaeniteAnimationFrameCount")
