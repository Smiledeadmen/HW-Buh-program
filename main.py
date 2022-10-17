from datetime import datetime
from application import salary as sal
from application.db import people
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print(datetime.today())
    sal.calculate_salary()
    people.get_employees()
    print("----------")
    plt.plot([1, 3, 2, 6, 1], [2, 1, 3, 6, 5])
    plt.show()
