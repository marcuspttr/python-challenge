# python-challenge
Practice in python coding reading csv files to help a bank with accounting and a polling station with results.

8/23/2021
Initial commit:
- Cloned repository to personal computer.
- Added PyBank and PyPoll folders.
  - Within each added: Resource & analysis folders as well as a main.py for the code.
  - Had to drag and drop the CSV files to copy into the respective Resource folders.

8/23/2021
Second commit:
- Wrote code for PyBank bank accounting problem.
- Was able to solve the required analysis; however, not very pleased with how I solved for the Average Change.
- Had to move CSV data for bank into the main folder as I could not get the proper reference for filepath:
  - I want it to be filepath = os.path.join('..','Resources','budget_data.csv') but it was not registering.

8/23/2021 10:09 am
Third commit:
- Wrote code for PyPoll vote analysis problem.
- Was able to solve for the indicated analysis.
- Similar issue and workaround for CSV data and filepath issues.

8/24/2021 6:17 pm
Fourth commit:
- Added code to both problems that allows them to output to a text file.
- This has a similar pathing issue to the csv files.


Current outstanding issues as of 8/24/2021, 6:17 pm
- Fix filepath problem to properly find data in Resource folders.
- Also need to fix text filepaths.

