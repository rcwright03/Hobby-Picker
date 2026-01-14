from sheet_code import hobby_sheet, getInput, getOutput

def main():
    # run function code here
    intensity, time, type = getInput()
    results_df = getOutput(intensity, time, type)

if __name__ == '__main__':
    main()