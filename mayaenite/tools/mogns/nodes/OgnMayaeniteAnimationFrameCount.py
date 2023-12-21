"""
This is the implementation of the OGN node defined in OgnMayaeniteAnimationFrameCount.ogn
"""

# Array or tuple values are accessed as numpy arrays so you probably need this import
import numpy
from pxr import Usd
import omni.usd
if False:
	from OgnMayaeniteAnimationFrameCountDatabase import OgnMayaeniteAnimationFrameCountDatabase

class OgnMayaeniteAnimationFrameCount:
	"""
	     Returns The Frame Count Of The Input Prim
	"""
	@staticmethod
	def compute(db) -> bool:
		"""Compute the outputs from the current input"""
		if False:
			isinstance(db,OgnMayaeniteAnimationFrameCountDatabase)
			
		#-------------------------------------------------------------------------------
		def get_Largest_TimeSamples_Lenght(prim:Usd.Prim):
			""""""
			sample_counts = []
			att = Usd.Attribute
			for att in prim.GetAttributes():
				if att.ValueMightBeTimeVarying():
					sample_counts.append(att.GetNumTimeSamples())
			if len(sample_counts):
				return max(sample_counts)
			else:
				return 0
		#-------------------------------------------------------------------------------
		def get_SkelAnimation_Frame_Count(prim:Usd.Prim,stage:Usd.Stage):
			frame_count = get_Largest_TimeSamples_Lenght(prim)
			tps   = stage.GetTimeCodesPerSecond()
			
			if db.inputs.useSceneFrameRate:
				fps   = stage.GetFramesPerSecond()
			else:
				fps   = db.inputs.frameRate
			
			calulated_frame_count = frame_count / (fps/tps)
			return int(calulated_frame_count)
		
		try:
			# With the compute in a try block you can fail the compute by raising an exception
			stage = omni.usd.get_context().get_stage()
			if len(db.inputs.prim):
				prim = stage.GetPrimAtPath(db.inputs.prim[0].pathString)
				db.outputs.frameCount = get_SkelAnimation_Frame_Count(prim,stage)
				db.outputs.outPrim = db.inputs.prim
		except Exception as error:
			# If anything causes your compute to fail report the error and return False
			db.log_error(str(error))
			return False

		# Even if inputs were edge cases like empty arrays, correct outputs mean success
		return True
