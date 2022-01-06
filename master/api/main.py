



class Permutation:
    """

    """
    def __init__(self, boxes, bullets,being_different_bullets=False, being_different_boxes=False, being_empty_boxes=False):
        self.boxes = boxes
        self.bullets = bullets
        self.being_different_bullets = being_different_bullets
        self.being_different_boxes = being_different_boxes
        self.being_empty_boxes = being_empty_boxes
        self.__status = 0

    @staticmethod
    def combination(n, k):
        """
            function to compute the number of combination of r objects out of n objects.
        """
        if (n == k):
            return 1
        if (k == 0):
            return 1
        return Permutation.combination(n - 1, k - 1) + Permutation.combination(n - 1, k)

    @staticmethod
    def factorial(n):
        """
            unction is used to calculate the factorial of a number n
        """
        res = 1
        if (n <= 1):
            return res
        for i in range(1, n + 1):
            res *= i
        return res

    @staticmethod
    def stirlingNumber(n, k):
        """
            function to calculate the Stirling numbers
        """
        if (k == n):
            return 1
        if (n == 0):
            return 0
        if (n == k - 1):
            return Permutation.combination(k, 2)
        if (k - n == 1):
            return Permutation.factorial(k - 1)
        return (Permutation.stirlingNumber(k - 1, n - 1)
                + (k - 1) * Permutation.stirlingNumber(k - 1, n))

    def __determined_status(self):
        """

        """
        if self.being_different_bullets:
            if self.being_different_boxes:
                if self.being_empty_boxes:
                    return 1
                else:
                    return 2
            else:
                if self.being_empty_boxes:
                    return 3
                else:
                    return 4
        else:
            if self.being_different_boxes:
                if self.being_empty_boxes:
                    return 5
                else:
                    return 6
            else:
                if self.being_empty_boxes:
                    return 7
                else:
                    return 8

    def get_resulte(self):
        """

        """
        self.__status = self.__determined_status()
        if self.__status == 1:
            return self.boxes ** self.bullets
        elif self.__status == 2:
            return Permutation.factorial(self.boxes) * Permutation.stirlingNumber(self.boxes, self.bullets)
        elif self.__status == 3:
            return Permutation.stirlingNumber(self.boxes, self.bullets)
        elif self.__status == 4:
            res = 0
            for i in range(self.boxes):
                res += Permutation.stirlingNumber(i, self.bullets)
            return res
        elif self.__status == 5:
            return Permutation.combination(self.bullets+self.boxes-1, self.boxes-1)
        elif self.__status == 6:
            return Permutation.combination(self.bullets-1, self.boxes-1)
        elif self.__status == 7 or self.__status == 8:
            return int(Permutation.factorial(self.bullets) / Permutation.factorial(self.bullets-self.boxes))
            # return Permutation.factorial(self.bullets-1)/Permutation.factorial(self.bullets-self.boxes) + Permutation.factorial(self.bullets-self.boxes)/Permutation.factorial(self.bullets-2*self.boxes)

