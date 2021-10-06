def arithmetic_arranger(problems, bool = False):
  number_of_problems = len(problems)

  if number_of_problems > 5:
    return "Error: Too many problems."
    quit()

  dash = "-"
  space = " "
  top_line = ""
  second_line = ""
  third_line = ""
  bottom_line = ""
  n=1

  for problem in problems:
    split_problem = problem.split()

    if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
      return "Error: Numbers cannot be more than 4 digits"
      quit()

    if len(split_problem[0]) + 2 > len(split_problem[2]) + 2:
      problem_width = len(split_problem[0]) + 2
    if len(split_problem[0]) + 2 <= len(split_problem[2]) + 2:
      problem_width = len(split_problem[2]) + 2

    if split_problem[1] != "+" and split_problem[1] != "-":
      return "Error: Operator must be '+' or '-'."
      quit()

    top_line = top_line + ((problem_width - len(split_problem[0])) * space) + split_problem[0] + 4*space

    second_line = second_line + split_problem[1] + (problem_width - len(split_problem[2]) - 1)*space + split_problem[2] + 4*space

    third_line = third_line + dash*problem_width + 4*space

    if bool == True:
      solution = 0
      try:
        first_number = int(split_problem[0])
        second_number = int(split_problem[2])
      except:
        return "Error: Numbers must only contain digits."
        quit()

      if split_problem[1] == "+":
        solution = first_number + second_number
      if split_problem[1] == "-":
        solution = first_number - second_number
      
      if n == 1:
        bottom_line = bottom_line + (problem_width - len(str(solution)))*space + str(solution)
      if n > 1:
        bottom_line = bottom_line + 4*space + (problem_width - len(str(solution)))*space + str(solution)

      n= n+1
      
  if bool == True:  
    arranged_problems = top_line + "\n" + second_line + "\n" + third_line + "\n" + bottom_line
  if bool == False: 
    arranged_problems = top_line + "\n" + second_line + "\n" + third_line

  return arranged_problems