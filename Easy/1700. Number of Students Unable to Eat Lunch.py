    class Solution:
      def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = 0
        zeros = 0
        for i in range(len(students)):
            if students[i] == 1:
                ones+=1
            else:
                zeros+=1
        for s in sandwiches:
            if s == 1 and ones > 0:
                ones-=1
            elif s == 0 and zeros > 0:
                zeros-=1
            else:
                return ones + zeros
        return 0