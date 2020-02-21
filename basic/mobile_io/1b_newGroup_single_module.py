import hebi
from time import sleep

lookup = hebi.Lookup()

# Wait 2 seconds for the module list to populate
sleep(2.0)

family_name = "HEBI" 
module_name = "Mobile IO"

group = lookup.get_group_from_names([family_name], [module_name])

if group is None:
  print('Group not found! Check that the family and name of a module on the network')
  print('matches what is given in the source file.')
  exit(1)

print('Created group from module {0} | {1}.'.format(family_name, module_name))
