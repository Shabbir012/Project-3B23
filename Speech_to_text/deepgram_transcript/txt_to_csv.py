import jpype
import asposecells

jpype.startJVM()
from asposecells.api import Workbook
# To convert txt file into csv
workbook = Workbook("C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Merged dataset.txt")
workbook.save("Merged.csv")
jpype.shutdownJVM()