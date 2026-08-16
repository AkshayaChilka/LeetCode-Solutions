class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0 = students.count(0)  # students preferring circular
        count1 = students.count(1)  # students preferring square
        
        for s in sandwiches:
            if s == 0:
                if count0 == 0:  # no one wants circular
                    return count1
                count0 -= 1
            else:
                if count1 == 0:  # no one wants square
                    return count0
                count1 -= 1
        
        return 0  # all students ate


        