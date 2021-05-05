require 'net/http'
require 'uri'

module Jekyll

  # Custom block for adding row and cols
  # This means BS <div class="row">...</div>
  # {% row %} starts a row to which {% col %} can be added
  class RowTagBlock < Liquid::Block
    
    def initialize(tag_name, markup, tokens)
      super
    end

    def render(context)
      site = context.registers[:site]
      converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
      output = converter.convert(super(context))
      "<div class=\"row\">#{output}</div>"
    end
  end

  # Custom block for adding a col - break point is BS md
  # {% col %} adds a 6 units column (default)
  # {% col 4 %} add a 4 units column
  class ColTagBlock < Liquid::Block
    
    def initialize(tag_name, size, tokens)
      super
      @size = size.to_i
      @size = (@size == 0) ? 6 : @size
    end

    def render(context)
      site = context.registers[:site]
      converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
      output = converter.convert(super(context))
      "<div class=\"col col-md-#{@size}\">#{output}</div>"
    end
  end

  # Custom block for wrapping content within <aside>
  class AsideTagBlock < Liquid::Block
    
    def initialize(tag_name, markup, tokens)
      super
      @warning = (markup.to_s.include? ".warning") ? "class=\"warning\"" : ""
    end

    def render(context)
      site = context.registers[:site]
      converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
      output = converter.convert(super(context))
      "<aside #{@warning}>#{output}</aside>"
    end
  end

  # Custom tag for checking if a file exits
  # The parmeter is the full-path from the site root
  # Return "true" is the file exists, "false" otherwise
  class FileExistsTag < Liquid::Tag

    def initialize(tag_name, path, tokens)
        super
        @path = path
    end

    def render(context)
        # Pipe parameter through Liquid to make additional replacements possible
        url = Liquid::Template.parse(@path).render context

        # Adds the site source, so that it also works with a custom one
        site_source = context.registers[:site].config['source']
        file_path = site_source + '/' + url

        # Check if file exists (returns true or false)
        "#{File.exist?(file_path.strip!)}"
    end
  end

  # Custom tag for remote includes from external sources.
  class RemoteInclude < Liquid::Tag

    def initialize(tag_name, remote_include, tokens)
      super
      @remote_include = remote_include
    end

    def open(url)
      Net::HTTP.get(URI.parse(url.strip)).force_encoding 'utf-8'
    end

    def render(context)
      # check if we passed a variable or directly a url
      url = @remote_include.to_s.match(/^ ?{{.*}} ?$/) ? context[@remote_include] : @remote_include
      open("#{url}")
    end

  end
end

Liquid::Template.register_tag('row', Jekyll::RowTagBlock)
Liquid::Template.register_tag('col', Jekyll::ColTagBlock)
Liquid::Template.register_tag('aside', Jekyll::AsideTagBlock)
Liquid::Template.register_tag('file_exists', Jekyll::FileExistsTag)
Liquid::Template.register_tag('remote_include', Jekyll::RemoteInclude)