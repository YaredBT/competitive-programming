class Solution(object):
        def fizzBuzz(self, n):
            i = 1
            my_list = []
            while i <= n:
                if i % 15 == 0:
                    my_list.append("FizzBuzz")
                elif i %3 == 0:
                    my_list.append("Fizz")
                elif i %5 == 0:
                    my_list.append("Buzz")
                else:
                    my_list.append(str(i))
                i += 1
            return my_list
