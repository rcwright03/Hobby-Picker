from sheet_code import hobby_sheet, getInput, getOutput, selectRandomActivities

def main():
    # run function code here
    intensity, time = getInput()
    results_df = getOutput(intensity, time)
    selectRandomActivities(results_df)

if __name__ == '__main__':
    main()