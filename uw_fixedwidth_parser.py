import string
import json

def parse_description(lines):
    s = ""
    for line in lines:
        if len(line) == 172:
            s += line.strip() + " "
    if not s:
        return ""
    return sentences


def parse_alt(line):
    if not line:
        return None
    date_time_location = str(line[24:56])
    if date_time_location[0:14] == "to be arranged":
        room = "TBD"
        building = "TBD"
        meeting_date = "TBD"
        meeting_times = "TBD"
        meeting_times_expl = []
    else:
        meeting_date = date_time_location[0:7].strip()
        meeting_times = date_time_location[7:18].strip()
        meeting_times_expl = meeting_times.split('-')
        building = date_time_location[18:23].strip()
        room = date_time_location[23:32].strip()

    return {'dayOfWeek': meeting_date, 'time': meeting_times, 'building': building, 'room': room}


def parse_first(lines):
    line = ""
    for l in lines:
        if len(l) == 121 or len(l) == 122:
            line = l

    if line.strip() == "":
        return
    data = {}
    raw_instr = str(line[0:6]).strip()
    add_code_required = True if str(line[6:7]) == '>' else False
    try:
        sln = int(line[7:12])
    except ValueError:
        pass
    section_id = str(line[12:16]).strip()
    credits = str(line[16:24]).strip()

    date_time_location = str(line[24:56])
    if date_time_location[0:14] == "to be arranged":
        room = "TBD"
        building = "TBD"
        meeting_date = "TBD"
        meeting_times = "TBD"
        meeting_times_expl = []
    else:
        meeting_date = date_time_location[0:7].strip()
        meeting_times = date_time_location[7:18].strip()
        meeting_times_expl = meeting_times.split('-')
        building = date_time_location[18:23].strip()
        room = date_time_location[23:32].strip()

    _d = {'dayOfWeek': meeting_date, 'time': meeting_times,
          'building': building, 'room': room}

    instructor = str(line[56:83]).strip().replace(",", ", ").title()
    if not instructor:
        instructor = "TBD"
    if ", " in instructor:
        instructor = instructor.split(", ")
        instructor = "{} {}".format(instructor[1].split(" ")[0], instructor[0])

    section_status = str(line[83:90]).strip()
    section_open = True if section_status == "Open" else False

    # print(line)
    print(line, "'{}'".format(line[90:94]))
    count_enrolled = int(line[90:94])
    count_limit = int(line[95:99])
    count_limit_estimated = True if line[99:100] == 'E' else False
    grading_policy = str(line[100:109]).strip()

    if instructor == "TBD" and credits == "LB":
        instructor = "(Lab section)"
    if instructor == "TBD" and credits == "QZ":
        instructor = "(Discussion section)"

    fee = line[109:114].strip().replace("$", "")
    fee = 0 if not fee else int(fee)

    return {
        'sln': sln,
        'sectionId': section_id,
        'primaryMeetingDate': meeting_date,
        'primaryMeetingTimes': meeting_times,
        'primaryBuilding': building,
        'primaryRoom': room,
        'instructor': instructor,
        'addCodeRequired': add_code_required,
        'gradingPolicy': grading_policy,
        'enrolled': count_enrolled,
        'limit': count_limit,
        'credits': credits,
        'isOpen': section_open,
        'materialsFee': fee,
        'times': [_d]
    }

    print("SLN {} {} / {} / {} / {} / {}".format(sln, section_id,
                                                 meeting_date, meeting_times_expl, building, room))
    print("Section is open: {} / Fee: ${}".format(section_open, fee))
    print("{} credits / Enrollment: {}/{}".format(credits,
                                                  count_enrolled, count_limit))
    print("Policy: {} / Instructor: {} / Add code: {}".format(grading_policy,
                                                              instructor, add_code_required))


#c = Course.from_record(' IS   >11665 A  5       to be arranged                                                       0/  15E                     ')
#c = Course.from_record(" IS   >11665 A  5       to be arranged                                                       0/  15E                     ")
