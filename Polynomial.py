class Polynomial(object):
    constant_of_integration = 2

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def return_order(self):
        return len(self.coefficients - 1)

    def add_polynomials(self, polynomial):
        coefficients1 = self.coefficients[:]
        coefficients2 = polynomial.coefficients[:]
        if len(coefficients1) > len(coefficients2):
            for i in range(len(coefficients2)):
                coefficients1[i] += coefficients2[i]
            return Polynomial(coefficients1)
        else:
            for i in range(len(coefficients1)):
                coefficients2[i] += coefficients1[i]
            return Polynomial(coefficients2)

    def differentiate(self):
        new_coefficients = []
        for i in range(1, len(self.coefficients)):
            new_coefficients.append(self.coefficients[i] * i)
        return Polynomial(new_coefficients)

    def integration(self):
        new_coefficients = [self.constant_of_integration]
        for i in range(len(self.coefficients)):
            new_coefficients.append(self.coefficients[i] / float(i + 1))
        return Polynomial(new_coefficients)

    def toString(self):
        polynomial = "P(x) = "
        for i in range(len(self.coefficients)):
            if i == 0:
                polynomial += str(self.coefficients[0]) + " "
            elif i == 1:
                polynomial += "+ " + str(self.coefficients[i]) + "x" + " "
            else:
                polynomial += "+ " + str(self.coefficients[i]) + "x^" + str(i) + " "
        polynomial += "\b"
        print(polynomial)


