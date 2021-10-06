def add_time(start, duration, starting_day="none"):
  import math

  day_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  split_start = start.split()
  split_duration = duration.split(":")

  number_of_days_passed = 0

  am_pm = split_start[1]

  start_time = split_start[0].split(":")
  start_hour = int(start_time[0])
  start_minute = int(start_time[1])

  duration_hour = int(split_duration[0])
  duration_minute = int(split_duration[1])

  if start_minute + duration_minute > 60:
    start_hour = start_hour + 1
    new_minute = start_minute + duration_minute - 60
  else:
    new_minute = start_minute + duration_minute
  if new_minute < 10:
    new_minute = "0{}".format(new_minute)


  if start_hour + duration_hour > 12:
    new_hour = (start_hour + duration_hour)%12
    am_pm_changes = math.floor((start_hour + duration_hour) / 12)
    while am_pm_changes > 0:
      if am_pm == "AM":
        am_pm = "PM"
      else:
        am_pm = "AM"
        number_of_days_passed = number_of_days_passed + 1
      am_pm_changes = am_pm_changes - 1
  else:
    new_hour = start_hour + duration_hour
  if new_hour == 0:
    new_hour = 12

  if starting_day == "none":
    if number_of_days_passed == 1:
      day = " (next day)"
    elif number_of_days_passed > 1:
      day = " ({} days later)".format(number_of_days_passed)
    elif number_of_days_passed < 1:
      day = ""  
  else:
    i = 0
    starting_day = starting_day.capitalize()
    while i < len(day_order):
      if starting_day == day_order[i]:
        day = day_order[i]
        break
      else:
        i = i + 1
    if number_of_days_passed + i <= len(day_order):
      day = day_order[i + number_of_days_passed - 1]
    else:
      day = day_order[((i+number_of_days_passed)%7) - 1]

  new_time = str(new_hour) + ":" + str(new_minute) + " {}".format(am_pm) + " {}".format(day)

  return new_time
