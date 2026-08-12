class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """st=[]
        for op in operations:
            if op == "C":
                st.pop()
            elif op == "D":
                st.append(2 * st[-1])
            elif op == "+":
                st.append(st[-1] + st[-2])
            else:
                st.append(int(op))
        return sum(st)"""

        st = []
        total = 0  # running sum

        for op in operations:
            if op == "C":
                total -= st.pop()
            elif op == "D":
                val = 2 * st[-1]
                st.append(val)
                total += val
            elif op == "+":
                val = st[-1] + st[-2]
                st.append(val)
                total += val
            else:
                val = int(op)
                st.append(val)
                total += val

        return total
