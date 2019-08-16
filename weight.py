# Variables

# pounds, feet
tractor_total = 21000
tractor_steers = 11800
tractor_drives = 9200
tractor_wheelbase = 20

# 5th wheel location, in feet, positive is front of center of drives
fifth_wheel = .25

# Tractor-trailer empty weights, pounds
trac_trlr_total = 35000
trac_trlr_steers = 12000
trac_trlr_drives = 12000
trlr_tandems = 11000

# Kingpin to center of trailer tandems, feet
kingpin_dist = 41

# Load weight, pounds
load = 44000

# Method

# Empty trailer weight, pounds
trlr_weight = trac_trlr_total - tractor_total

# Find centroid of empty trailer
trlr_xbar = kingpin_dist - ((kingpin_dist * trlr_tandems) / trlr_weight)

# Find centroid of tractor
tractor_xbar = (tractor_wheelbase * tractor_steers) / tractor_total

# Choose load location, distance from trailer tandems
# load_xbar = 20.5
load_xbar = 20

# Loaded trailer:

# Solve for normal force on kingpin, A
nf_kingpin = ((trlr_xbar * trlr_weight) + (load_xbar * load)) / kingpin_dist

# Solve for normal force on steers, A2
nf_steers = ((fifth_wheel * nf_kingpin) + (tractor_xbar * tractor_total)) / tractor_wheelbase

# Solve for normal force on drives, A1
nf_drives = nf_kingpin + tractor_total - nf_steers

# Solve for normal force on loaded trailer tandems, B
nf_trlr_tandems = load + trac_trlr_total - nf_drives - nf_steers

print("Steers: ", round(nf_steers))
print("Drives: ", round(nf_drives))
print("Trailer Tandems: ", round(nf_trlr_tandems))
