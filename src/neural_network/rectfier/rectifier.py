import cv2
import numpy as np

# Code adapted from
# https://github.com/felipeadsm/rectification-and-extraction-of-chars-from-images/blob/main/Rectify.py#L5


class Rectifier:

    @staticmethod
    def rectify(image_source):
        try:
            areas = []
            list_points = []
            area_aux = 0
            points_aux = 0
            point1 = 0
            point4 = 0
            aux1 = []
            aux2 = []

            grayimg = cv2.cvtColor(image_source, cv2.COLOR_BGR2GRAY)
            binimg = cv2.Canny(grayimg, 110, 200, 3)
            cv2.imshow('Canny', binimg)
            cv2.waitKey(0)
            dkernel = np.ones((5, 5))
            ekernel = np.ones((3, 3))
            img_dilate = cv2.dilate(binimg, dkernel, iterations=1)
            img_erode = cv2.erode(img_dilate, ekernel, iterations=1)
            cv2.imshow('dilate/erode', img_erode)
            cv2.waitKey(0)
            contours, _ = cv2.findContours(
                img_dilate,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE,
            )
            copyimg = image_source.copy()
            cv2.drawContours(copyimg, contours, -1, (0, 255, 0), 3)
            cv2.imshow('Countours', copyimg)
            cv2.waitKey(0)
            for c in contours:
                area = cv2.contourArea(c)
                areas.append(area)
                perimeter = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
                list_points.append(approx)

            i = 0
            for n in areas:
                if n > area_aux:
                    area_aux = n

                    if len(list_points[i]) == 4:
                        points_aux = list_points[i]

                i = i + 1

            sum0 = points_aux[0, 0, 0] + points_aux[0, 0, 1]
            sum1 = points_aux[1, 0, 0] + points_aux[1, 0, 1]
            sum2 = points_aux[2, 0, 0] + points_aux[2, 0, 1]
            sum3 = points_aux[3, 0, 0] + points_aux[3, 0, 1]

            bigger = max([sum0, sum1, sum2, sum3])
            smaller = min([sum0, sum1, sum2, sum3])

            if bigger == sum0:
                point4 = [points_aux[0, 0, 0], points_aux[0, 0, 1]]
                sum0 = 0
            elif bigger == sum1:
                point4 = [points_aux[1, 0, 1], points_aux[1, 0, 1]]
                sum1 = 0
            elif bigger == sum2:
                point4 = [points_aux[2, 0, 0], points_aux[2, 0, 1]]
                sum2 = 0
            elif bigger == sum3:
                point4 = [points_aux[3, 0, 0], points_aux[3, 0, 1]]
                sum3 = 0

            if smaller == sum0:
                point1 = [points_aux[0, 0, 0], points_aux[0, 0, 1]]
                sum0 = 0
            elif smaller == sum1:
                point1 = [points_aux[1, 0, 0], points_aux[1, 0, 1]]
                sum1 = 0
            elif smaller == sum2:
                point1 = [points_aux[2, 0, 0], points_aux[2, 0, 1]]
                sum2 = 0
            elif smaller == sum3:
                point1 = [points_aux[3, 0, 0], points_aux[3, 0, 1]]
                sum3 = 0

            list_sum = [sum0, sum1, sum2, sum3]

            for n in list_sum:
                if n == 0:
                    list_sum.remove(n)

            if list_sum[0] == sum0:
                aux1 = [points_aux[0, 0, 0], points_aux[0, 0, 1]]
            elif list_sum[0] == sum1:
                aux1 = [points_aux[1, 0, 0], points_aux[1, 0, 1]]
            elif list_sum[0] == sum2:
                aux1 = [points_aux[2, 0, 0], points_aux[2, 0, 1]]
            elif list_sum[0] == sum3:
                aux1 = [points_aux[3, 0, 0], points_aux[3, 0, 1]]

            if list_sum[1] == sum0:
                aux2 = [points_aux[0, 0, 0], points_aux[0, 0, 1]]
            elif list_sum[1] == sum1:
                aux2 = [points_aux[1, 0, 0], points_aux[1, 0, 1]]
            elif list_sum[1] == sum2:
                aux2 = [points_aux[2, 0, 0], points_aux[2, 0, 1]]
            elif list_sum[1] == sum3:
                aux2 = [points_aux[3, 0, 0], points_aux[3, 0, 1]]

            if aux1[0] > aux2[0]:
                point2 = aux1
                point3 = aux2
            else:
                point3 = aux1
                point2 = aux2

            list_out = [point1[0], point1[1], point2[0], point2[1],
                        point3[0], point3[1], point4[0], point4[1]]
            print(list_out)
            points_in = np.float32([[list_out[0], list_out[1]],
                                    [list_out[2], list_out[3]],
                                    [list_out[4], list_out[5]],
                                    [list_out[6], list_out[7]]])
            points_out = np.float32([[0, 0], [640, 0],
                                    [0, 480], [640, 480]])
            matrix = cv2.getPerspectiveTransform(points_in, points_out)
            rectified = cv2.warpPerspective(image_source, matrix, (640, 480))
            cv2.imshow('Rectified Img', rectified)
            cv2.waitKey(0)
            return rectified
        except Exception as e:
            print(e)
            return image_source
