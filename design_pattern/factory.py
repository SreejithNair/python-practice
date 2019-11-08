def resized_image(self, src, w, h):
    resize_image = cv2.resize(src, (w, h), interpolation=cv2.INTER_CUBIC)
    return resize_image

def showall(self):
    global b
    try:
        img1 = cv2.imread(image)
        h1, w1, c1 = img1.shape
        img2 = cv2.imread(self.img2)
        h2, w2, c2 = img2.shape
        arr = []  # create empty list
        if self.count_cbox.currentText() == "2":
            if self.merge_cbox.currentText() == "Horizontal":
                self.axis = 1
                if h1 >= h2:
                    factor = h1 / h2
                    arr.append(self.resized_image(img1, w1, h1))
                    arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))

                elif h2 >= h1:
                    factor = h2 / h1
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, w2, h2))
            elif self.merge_cbox.currentText() == "Vertical":
                self.axis = 0
                if w1 >= w2:
                    factor = w1 / w2
                    arr.append(self.resized_image(img1, w1, h1))
                    arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))

                elif w2 >= w1:
                    factor = w2 / w1
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, w2, h2))
        elif self.count_cbox.currentText() == "3":
            img3 = cv2.imread(self.img3)
            h3, w3, c3 = img3.shape
            if self.merge_cbox.currentText() == "Horizontal":
                self.axis = 1
                if h1 >= h2 and h1 >= h3:
                    factor = h1 / h2
                    factor2 = h1 / h3
                    arr.append(self.resized_image(img1, w1, h1))
                    arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))
                    arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))

                elif h2 >= h1 and h2 >= h3:
                    factor = h2 / h1
                    factor2 = h2 / h3
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, w2, h2))
                    arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))
                else:
                    factor = h3 / h1
                    factor2 = h3 / h2
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, int(w2 * factor2), int(h2 * factor2)))
                    arr.append(self.resized_image(img3, w3, h3))
            elif self.merge_cbox.currentText() == "Vertical":
                self.axis = 0
                if w1 >= w2 and w1 >= w3:
                    factor = w1 / w2
                    factor2 = w1 / w3
                    arr.append(self.resized_image(img1, w1, h1))
                    arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))
                    arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))

                elif w2 >= w1 and w2 >= w3:
                    factor = w2 / w1
                    factor2 = w2 / w3
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, w2, h2))
                    arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))
                else:
                    factor = w3 / w1
                    factor2 = w3 / w2
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, int(w2 * factor2), int(h2 * factor2)))
                    arr.append(self.resized_image(img3, w3, h3))

        for i in enumerate(arr):
            b = np.concatenate((arr), axis=self.axis)