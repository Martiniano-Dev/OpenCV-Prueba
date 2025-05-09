import cv2

imagenarchivo = ''

umbral = 150

img = cv2.imread(imagenarchivo)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img3 = cv2.threshold(img2, umbral, 255, cv2.THRESH_BINARY)

cv2.imshow("Imagen", img)

cv2.imshow("Imagen Gris", img2)

cv2.imshow("Imagen Binaria", img3)

edges = cv2.Canny(img2, 100, 200)

superior = 200

cv2.imshow("Imagen bordes Canny",edges)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Número de contornos detectados:", len(contours))

img_contours = cv2.drawContours(img.copy(), contours, -1, (255, 0, 0), 1)

cv2.imshow("Imagen con contornos",img_contours)


cv2.waitKey(0)
cv2.destroyAllWindows()