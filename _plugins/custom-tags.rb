module Jekyll
  class AsideTagBlock < Liquid::Block
    
    def initialize(tag_name, markup, tokens)
      super
    end

    def render(context)
      site = context.registers[:site]
      converter = site.find_converter_instance(::Jekyll::Converters::Markdown)
      output = converter.convert(super(context))
      "<aside>#{output}</aside>"
    end
  end
end
  
Liquid::Template.register_tag('aside', Jekyll::AsideTagBlock)