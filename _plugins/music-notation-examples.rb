
module Jekyll
  class MusicNotationExamples < Generator
    safe true
    priority :high

    def generate(site)

      # Store an array of all examples we have in the book
      examples = []
      # The path to the inclue
      meiExamples = site.source + "/_includes/"
      svgExamples = site.source + "/images/"
      
      # The only collection we want to process
      book = site.collections['book']
      # Sort it by path
      book.docs.sort_by(&:path).each do |doc|
        # Remove the absolute part of the path
        short_path = doc.path.gsub(book.directory, "")

        if doc.data['examples']
          # The path for an example is base on the directory of the file it is in.
          example_path = get_example_path_for(short_path)
          doc.data['examples'].each do |example|
            # The SVG and the MEI snippet files
            svgFile = example_path + example['name'] + ".svg"
            meiFile = example_path + example['name'] + ".mei"
            # Add them to the example list
            example['mei-example-file'] = meiFile
            example['svg-example-file'] = svgFile
            examples.push(example)
            # Here check if the file exists. If not, it means it still need to be generated with the 
            # file need to be generated with ./scripts/generate-examples.py
            # The flags set here are to inform the _include/music-notation template not to actually include them
            puts svgExamples + svgFile
            puts meiExamples + meiFile
            example['svg-example-exists'] = true unless (!File.exists?(svgExamples + svgFile))
            example['mei-example-exists'] = true unless (!File.exists?(meiExamples + meiFile))
          end
        end
      end

      # Generate an input file for the ./scripts/generate-examples.py
      path = File.expand_path "scripts/examples.yaml", site.source
      File.open(path, 'w') { |file| file.write(examples.to_yaml) }
    end

    def get_example_path_for(path)
      example_path = "examples"
      return example_path + path.gsub(/[^\/]*$/,"")
    end

  end
end