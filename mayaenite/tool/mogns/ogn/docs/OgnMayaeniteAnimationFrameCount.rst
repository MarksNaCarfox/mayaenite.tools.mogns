.. _MayaeniteToolMognsExtension_MayaeniteAnimationFrameCount_1:

.. _MayaeniteToolMognsExtension_MayaeniteAnimationFrameCount:

.. ================================================================================
.. THIS PAGE IS AUTO-GENERATED. DO NOT MANUALLY EDIT.
.. ================================================================================

:orphan:

.. meta::
    :title: Mayaenite Animation Frame Count
    :keywords: lang-en omnigraph node Mayaenite mayaenitetoolmognsextension mayaenite-animation-frame-count


Mayaenite Animation Frame Count
===============================

.. <description>

Returns The Frame Count Of The Input Prim

.. </description>


Installation
------------

To use this node enable :ref:`mayaenite.tool.mogns<ext_mayaenite_tool_mogns>` in the Extension Manager.


Inputs
------
.. csv-table::
    :header: "Name", "Type", "Descripton", "Default"
    :widths: 20, 20, 50, 10

    "Frame Rate (*inputs:frameRate*)", "``timecode``", "The Frame Rate The Animation Was Generated At", "24.0"
    "Prim (*inputs:prim*)", "``target``", "The Prim To Get The Frame Count For", "0"
    "Use Scene Frame Rate (*inputs:useSceneFrameRate*)", "``bool``", "When checked this node will use the frame rate of the root layer", "False"


Outputs
-------
.. csv-table::
    :header: "Name", "Type", "Descripton", "Default"
    :widths: 20, 20, 50, 10

    "Frame Count (*outputs:frameCount*)", "``int``", "The Amount Of Frames The Input Prim Has", "None"
    "Prim (*outputs:outPrim*)", "``target``", "outputs the input path for exe flow into down streem inputs", "None"


Metadata
--------
.. csv-table::
    :header: "Name", "Value"
    :widths: 30,70

    "Unique ID", "MayaeniteToolMognsExtension.MayaeniteAnimationFrameCount"
    "Version", "1"
    "Extension", "mayaenite.tool.mogns"
    "Has State?", "False"
    "Implementation Language", "Python"
    "Default Memory Type", "cpu"
    "Generated Code Exclusions", "None"
    "uiName", "Mayaenite Animation Frame Count"
    "Categories", "Mayaenite"
    "__categoryDescriptions", "Mayaenite,Nodes implementing lights for rendering"
    "Generated Class Name", "OgnMayaeniteAnimationFrameCountDatabase"
    "Python Module", "mayaenite.tool.mogns"

