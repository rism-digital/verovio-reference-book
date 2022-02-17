=begin
  Jekyll Hook generates a pages.json file for indexing with lunr.js

  Applies to all pages and all posts in .md and .html files

  A page can be exlude from indexing with a search_exclude: true in the frontmatter
  A page can be indexed in all languages with a index_all_lang: true in the frontmatter
=end

require 'json'

# The index file we are generated
@pagesFile = "_site/pages.json"
# The array to which we add index entries
@pages = []
# A counter of documents for index id
@counter = 0
# The site for accessing the site.active_lang status
@site = nil

Jekyll::Hooks.register :site, :after_reset do |site, payload|
    File.delete(@pagesFile) if File.exist?(@pagesFile)
    puts "Delete index file"
    @site = site
    @pages = []
end
  
Jekyll::Hooks.register :site, :post_write do |site|
    puts "Writing index file"
    File.open(@pagesFile, "w") { |f| f.write @pages.to_json }
end

Jekyll::Hooks.register :documents, :post_write do |page|
    indexDoc(page)
end

def indexDoc(doc)

    docExt = doc.extname.tr('.', '')
    # only process if we deal with a markdown or html file
    return if (docExt != 'md' && docExt != 'html')

    # skip excluded pages
    return if (doc.data['search_exclude'])
    
    docData = nil
    docTitle = doc.data['title']

    # remove html markup
    re = /<("[^"]*"|'[^']*'|[^'">])*>/
    docData = doc.content.gsub(re, '') if doc.content
    return if (!docData | !docTitle)
    # remove additional characters
    docData.gsub!("\n", " ")
    docData.gsub!("    ", " ")
    docData.strip!
    docData.gsub!(/\s+/, " ")

    # remove characters from the title too
    docTitle.gsub!("    ", " ")

    # create the json object for the index entry
    page = Hash.new
    page['id'] = @counter
    page['title'] = docTitle
    page['url'] = doc.url
    page['body'] = docData
    @pages << page

    @counter += 1
end
  