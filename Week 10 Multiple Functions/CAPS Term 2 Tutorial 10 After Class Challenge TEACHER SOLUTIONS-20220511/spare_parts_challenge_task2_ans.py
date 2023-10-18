"""
The part number, the name of the supplier, the number bought, the number sold
"""
XP22 = ['XP22', 'Butterworth', 400, 43]
FG54 = ['FG54', 'Jung Machinery', 100, 35]
CTM87 = ['CTM87', 'Tan Automation', 150, 120]
LLL39 = ['LLL39', 'Butterworth', 50, 28]
PQ903 = ['PQ903', 'Tan Automation', 200, 199]
UY4 = ['UY4', 'Jung Machinery', 100, 98]
CTM99 = ['CTM99', 'Jung Machinery', 280, 266]
AM69 = ['AM69', 'Prefachine', 150, 62]
CX324 = ['CX324', 'AI Machinery', 200, 60]
YLD34 = ['YLD34', 'Prefachine', 125, 39]
XG65 = ['XG65', 'AI Machinery', 160, 74]
WF91 = ['WF91', 'Butterworth', 120, 12]
VF83 = ['VF83', 'Butterworth', 90, 45]
TTM = ['TTM', 'AI Machinery', 175, 31]
SQ87 = ['SQ87', 'Tan Automation', 200, 54]
spare_parts = [XP22, FG54, CTM87, LLL39, PQ903, UY4, CTM99, AM69, CX324, YLD34, XG65, WF91, VF83, TTM, SQ87]


# a function to determine the status of a part
def part_status(part):
    if part[1] == 'Jung Machinery':
        status = 'Repurchase'
    elif part[3] / part[2] < 0.4:
        status = 'Discontinue'
    elif part[1] == 'Tan Automation' or part[1] == 'Butterworth' \
            or part[1] == 'AI Machinery':
        status = 'Review'
    else:
        status = 'Repurchase'
    return status


print('Part\tBought\tSold\tUnsold\t%\tSupplier\tStatus')
for part in spare_parts:
    print('%s\t%d\t%d\t%d\t%.1f\t%s\t%s' \
          % (part[0], part[2], part[3], part[2] - part[3], part[3] / part[2] * 100, \
             part[1], part_status(part)))
