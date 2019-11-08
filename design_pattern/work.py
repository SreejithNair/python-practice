from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self, h1, h2, img1, img2) -> str:
        self.axis = 1
                if h1 >= h2:
                    factor = h1 / h2
                    arr.append(self.resized_image(img1, w1, h1))
                    arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))

                elif h2 >= h1:
                    factor = h2 / h1
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, w2, h2))
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
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
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
          self.axis = 0
                if w1 >= w2:
                    factor = w1 / w2
                    arr.append(self.resized_image(img1, w1, h1))
                    arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))

                elif w2 >= w1:
                    factor = w2 / w1
                    arr.append(self.resized_image(img1, int(w1 * factor), int(h1 * factor)))
                    arr.append(self.resized_image(img2, w2, h2))
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
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
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())