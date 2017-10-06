# About the script

The script can be used to check for the correctness of the README.md file

# Command to run the script

    python parse_readme.py README.md

# Sample output 1

Output when a README file in proper yaml format is supplied:

The file is in a valid yaml format

###############################################################################
# yaml
###############################################################################
Project:
  URL: null
  abstract: TBD
  author:
  - Vegi, Karthik
  pid:
  - 0
  status: not started
  title: TBD
  type: latex
owner:
  hid: 231
  name: Vegi, Karthik
  url: https://github.com/bigdata-i523/hid231
paper1:
  abstract: 'This paper intends to discuss how Big Data can be used to spot fake news,
    bad data used by politicians, advertisers, and scientists.

    '
  author:
  - Vegi, Karthik
  chapter: Media
  hid:
  - 231
  status: In progress
  title: Using Big Data for Fact Checking
  type: latex
  url: https://github.com/bigdata-i523/hid231/paper1/report.pdf
paper2:
  abstract: This paper will focus on how we can combat air pollution using the technology
    advancements in big data, cloud computing, and IOT
  author:
  - Vegi, Karthik
  chapter: Media
  hid:
  - 231
  status: Not started
  title: Using Big Data to battle Air Pollution
  type: latex
  url: https://github.com/bigdata-i523/hid231/paper2/report.pdf

    
# Sample output 2

Output when a README file in incorrect yaml format is supplied:

ERROR: The file is not in a valid yaml format
