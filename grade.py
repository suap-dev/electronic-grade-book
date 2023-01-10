from typing import Literal
from typeguard import typechecked

class Grade:
    __slots__ = ['__grade', '__weight', '__comment', '__valid', '__invalidation_reason']

    # TODO: Do something so that we got intermediate thingies.
    # TODO: maybe a field for just "plus" ? have to think about it.
    __grades = Literal[
        '1',
        '1+',
        '2',
        '2+',
        '3',
        '3+',
        '4',
        '4+',
        '5',
        '5+',
        '6'
    ]
    # grades = Literal(__grades_list)
    weights = Literal[1, 2, 3, 4]
    
    @typechecked
    def __init__(self, grade: __grades, weight: weights=1, comment: str=None) -> None:
        
        self.__grade = grade
        self.__weight = weight
        # TODO: dateime automaticaly added to comment while created
        self.__comment = comment
        
        self.__valid = True
        self.__invalidation_reason = None
        
    
    def get_grade(self) -> str:
        return self.__grade
    
    def get_weight(self) -> int:
        return self.__weight
    
    def get_comment(self) -> str:
        return self.__comment
    
    def is_valid(self) -> bool:
        return self.__valid
    
    def get_value(self) -> float:
        if(self.__valid):
            grade = int(self.__grade[0])
            plus = 0.5 if len(self.__grade) > 1 else 0
            return self.__weight*(grade + plus)
        else:
            return 0
    
    @typechecked
    def change_weight(self, weight: weights) -> None:
        # TODO: Exeception?
        if self.__valid:
            self.__weight = weight
        else:
            print('Grade invalidated. Cannot change.')    
    
    @typechecked
    def add_comment(self, comment: str) -> None:
        # TODO: Exeception?
        if self.__valid:
            # TODO: datetime automaticaly added to edit
            # TODO: change comments section to list
            self.__comment += '; ' + comment
        else:
            print('Grade invalidated. Cannot change.')
            
    @typechecked
    def invalidate(self, reason) -> None:
        # TODO: Exeception?
        if self.__valid:
            self.__valid = False
            self.__invalidation_reason = reason
        else:
            print('Grade invalidated. Cannot change.')
            
            
    # def something(self):                
    #     message = ''
          
    #     if not self.__valid:
    #         message += 'Invalidated: ' + self.__invalidation_reason + ', '     
                   
    #     message += 'grade: ' + self.__grade + ', weight: ' + str(self.__weight)        
        
    #     if self.__comment:
    #         message += ', comment: ' + self.__comment       
                 
    #     return message
    
    def __repr__(self) -> float:
        return f"Grade(grade={repr(self.__grade)}, weight={self.weight}, comment={self.__comment})"
    
    def __str__(self) -> str:                
        message = ''
          
        if not self.__valid:
            message += 'Invalidated: ' + self.__invalidation_reason + ', '     
                   
        message += 'grade: ' + self.__grade + ', weight: ' + str(self.__weight)        
        
        if self.__comment:
            message += ', comment: ' + self.__comment
            
        return message
        
    grade   = property(get_grade)
    weight  = property(get_weight, change_weight)
    comment = property(get_comment, add_comment)
    valid   = property(is_valid)
    value   = property(get_value)    
       
if __name__ == '__main__':
    grades_list = []
    nr_of_grades = int(input("How many grades you're going to add? "))

    for nr in range(nr_of_grades):
        grade  = input("Grade:  ")
        def get_weight(w):
            if w in [1, 2, 3, 4]: return w        
            else: return 1    
        weight = get_weight(input("Weight: "))
        grades_list.append(Grade(grade, weight))
        
    sum_of_values = 0
    sum_of_weights = 0
    for grade in grades_list:
        sum_of_values  += grade.value
        sum_of_weights += grade.weight
        
    print("The mean is", sum_of_values/sum_of_weights)