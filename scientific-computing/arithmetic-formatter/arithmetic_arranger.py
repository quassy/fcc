def arithmetic_arranger(
    problems: list,
    answer: bool = False,
) -> str:
    if len(problems) > 5:
        return "Error: Too many problems."
    rows = ["", "", "", ""]
    for index, problem in enumerate(problems):
        first, operator, second = problem.split(" ")
        if operator in ["*", "/"]:
            return "Error: Operator must be '+' or '-'."
        max_len = max(len(first), len(second))
        if max_len > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            first = int(first)
            second = int(second)
        except ValueError:
            return "Error: Numbers must only contain digits."
        result = first + second if operator == "+" else first - second
        rows[0] += f" {first:>{max_len+1}}"
        rows[1] += f"{operator}{second:>{max_len+1}}"
        rows[2] += "-" * (max_len + 2)
        rows[3] += f" {result:>{max_len+1}}"
        if index == (len(problems) - 1):
            break
        rows[0] += "    "
        rows[1] += "    "
        rows[2] += "    "
        rows[3] += "    "
    if answer == False:
        rows.pop()
    arranged_problems = "\n".join(rows)
    return arranged_problems
