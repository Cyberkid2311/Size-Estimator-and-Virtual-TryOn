from customer import grabcut, userPreprocess 
import cv2
import os
import sys
from apparel import catPreprocess
from join import userFit

print("Press 's' when you are done with final TouchUps")
if not os.path.exists('Bits & Pieces/'):
	os.makedirs('Bits & Pieces/')

img = cv2.imread(sys.argv[1])
grabInst = grabcut(img)
grabcutOutput = grabInst.grabcut()
cv2.imwrite("Bits & Pieces/initialApparel.png",grabcutOutput)

processInst = userPreprocess(grabcutOutput)
processInst.cropImg()
processOut = processInst.removeTurds()

processInst.segImage(processOut)
LU, RU = processInst.getSegLines()

leftArmUser = processInst.armSegment(processOut,'left')
cv2.imwrite('Bits & Pieces/CustomerLeftArm.png',leftArmUser)
rightArmUser = processInst.armSegment(processOut,'right')
cv2.imwrite('new/CustomerRightArm.png',rightArmUser)

catImg = cv2.imread(sys.argv[2])
catInst = catPreprocess(catImg)
floodOut = catInst.edgeDetect()
cv2.imwrite("Bits & Pieces/NewApparel.png",floodOut)
cropFlood = catInst.cropImg(floodOut)
catInst.segImage(cropFlood)
LC, RC = catInst.getSegLines()
cv2.imwrite("Bits & Pieces/NewApparelCropped.png",cropFlood)

rightArmCat = catInst.armSegment(cropFlood,'right')
cv2.imwrite('Bits & Pieces/NewApparelRightArm.png',rightArmCat)
leftArmCat = catInst.armSegment(cropFlood,'left')
cv2.imwrite('Bits & Pieces/NewApparelLeftArm.png',leftArmCat)

fitInst = userFit(processOut,cropFlood)
fitInst.setSegLines(LC,RC,LU,RU)
colorUserOut = fitInst.colorUser()
cv2.imwrite('Bits & Pieces/NewApparelColor.png',colorUserOut)

fitInst.setUserArm(leftArmUser,rightArmUser)
fitInst.setCatArm(leftArmCat,rightArmCat)
fitLeft, fitRight = fitInst.sleeveFit()
cv2.imwrite('Bits & Pieces/NewApparelLeftFit.png',fitLeft)
cv2.imwrite('Bits & Pieces/NewApparelRightFit.png',fitRight)

bodyFitOut = fitInst.bodyFit(colorUserOut)
cv2.imwrite('Bits & Pieces/RantOn_Fit.png',bodyFitOut)
finalFit = fitInst.finalFit(bodyFitOut,fitLeft,fitRight)
cv2.imwrite('Bits & Pieces/RantOn_FinalFit.png',finalFit)
fitInst.setUserBox(processInst.returnUserBox())

output = fitInst.fittingOntoUser(finalFit,cv2.imread(sys.argv[1]))
cv2.imwrite('RantOn_TryOn.jpg',output)
#---------------------END OF CODE--------------------------------#