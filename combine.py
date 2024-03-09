import os

def combine_mdx_files(directory, output_file):
    mdx_content = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mdx"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as mdx_file:
                    mdx_content.append(mdx_file.read())

    combined_content = "\n".join(mdx_content)

    with open(output_file, "w") as output:
        output.write(combined_content)

    print(f"Combined MDX files saved as '{output_file}'.")

# Specify the directory to search for MDX files
directory = "."

# Specify the output file name
output_file = "combined.mdx"

combine_mdx_files(directory, output_file)
