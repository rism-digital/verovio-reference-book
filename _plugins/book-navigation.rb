require "nokogiri"

module Jekyll
  # Allow for a document to have its url replaced
  class Document
    def url=(name)
      @url = name
    end
  end

  class BookNavigation < Generator
    safe true
    priority :high

    def generate(site)

      # We use the parse to add h3 (###) item to the toc
      @parser = Jekyll::Converters::Markdown.new(site.config)

      # A map of url => chapter_id 
      # Used for retrieving the chapter_id when processing a doc in liquid
      chapters = Hash.new
      # A map of url => section_id
      sections = Hash.new
      # An array of top-level (chapters) items
      # Recursively contains section and subsections
      toc = Array.new

      # The only collection we want to process
      book = site.collections['book']
      # Sort it by path
      book.docs.sort_by(&:path).each do |doc|
        # Remove the dd- (numbers) from the url
        url = doc.url.gsub(/\d\d-/,"")
        # Remove the root /book from the url
        url = url.gsub(/^\/book/,"")
        # Remove index.html
        url = url.gsub(/\/index.html$/,"/")
        # Set it
        doc.url = url

        # Remove the absolute part of the path
        short_path = doc.path.gsub(book.directory, book.relative_directory)

        chapter_id = get_chapter(short_path)
        section_id = get_section(short_path)

        # Something must be wrong...
        if (!chapter_id or !section_id)
          puts "Missing chapter"
          next
        end

        # This is a chapter doc
        if (section_id == '00-index')
          # Sections are empty for now
          toc.push({"id" => chapter_id, "name" => doc['chapter-title'], "url" => url, "sections" => [], "link_to_section" => doc.data['link_to_section']})
          chapters[short_path] = chapter_id
        end

        chapters[short_path] = chapter_id
        sections[short_path] = section_id

        # Retrieve the chapter to which the section belongs
        sectionChapter = toc.select{ |c| c['id'] == chapter_id }
        # Something must be wrong - we do need to have a chapter doc
        if (!sectionChapter)
          puts "Missing chapter for section"
          next
        end

        # We can add subsection directly when adding the section
        sectionChapter[0]['sections'].push({"id" => section_id, "name" => doc['title'], "url" => url, "subsections" => get_subsection_array(doc)})
      end

      # Chapters can have a member 'link_to_section'.
      # When set to true, we want the link in the toc to directly show the first
      # section of the chapter. We adjust the url of the chapter here
      toc.each do |chapter|
        if chapter['link_to_section'] && chapter['sections'].size > 1
          chapter['url'] = chapter['sections'][1]['url']
          chapter['sections'].shift
        end
      end

      site.data['toc'] = toc
      site.data['chapters'] = chapters
      site.data['sections'] = sections

      # Generate the script/toc.yaml file with a hash url => name
      # Used by generate-options.py to add approriate labels to references
      toc_hash = Hash.new
      toc.each do |chapter|
        # chapter url => name
        toc_hash[chapter['url']] = chapter['name']
        chapter['sections'].each do |section|
          # section url => name
          toc_hash[section['url']] = section['name']
          section['subsections'].each do |subsection|
            # section url + # + subsection hash => name
            toc_hash["#{section['url']}##{subsection['hash']}"] = subsection['name']
          end
        end
      end
      path = File.expand_path "scripts/toc.yaml", site.source
      file = File.open(path, 'w') { |file| file.write(toc_hash.to_yaml) }

    end

    def get_chapter(path)
      if (path.count('/') < 1)
        return nil
      end
      return path.gsub(/^[^\/]*\//,"").gsub(/\/.*/,"").gsub(/.md$/,"")
    end

    def get_section(path)
      if (path.count('/') < 2)
        return nil
      end
      return path.gsub(/^[^\/]*\/[^\/]*\//,"").gsub(/\/.*/,"").gsub(/.md$/,"")
    end

    def get_subsection_array(doc)
      subsections = Array.new
      html = Nokogiri::HTML(@parser.convert(doc.content))
      html.css('h3').each do |heading|
        subsections.push({"name" => heading.text, "hash" => heading['id']})
      end
      return subsections
    end

  end
end