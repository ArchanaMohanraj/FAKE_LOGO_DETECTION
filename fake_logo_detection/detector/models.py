import cv2

def fakeDetector(path):
    path = path.split('\\')
    filename = path.pop()
    path = '\\'.join(path)
    path += '\\media\\' + filename

    img1 = cv2.imread(path, 0)
    img2 = cv2.imread("C:\\Users\\ARCHANA MOHANRAJ\\OneDrive - Kumaraguru College of Technology\\Desktop\\archive\\A\\amazon\\22.png", 0)
    print(img1)
    print(img2)
    orb = cv2.ORB_create(nfeatures=1000)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    print(len(good))
   

    # img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
    # cv2.imshow('img1', img1)
    # cv2.imshow('img2', img2)
    # cv2.imshow('img3', img3)
    # cv2.waitKey(0)
    
    if(len(good) >= 500):
        return True
    else:
        return False     