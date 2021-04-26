Jekyll::Hooks.register :site, :after_init do |site| 
    if site.config['generate-full-chapters']
        STDOUT.write "Enable PDF generation\n"
        @generate_pdf = true
    end
end

Jekyll::Hooks.register :documents, :post_render do |doc| 
    if @pdf_page
        STDOUT.write "Adding page content to PDF\n"
        if doc.data['chapter-title']
            @pdf_page.content += "<h1>#{doc.data['chapter-title']}</h1>\n\n"
        end
        if doc.data['title'] != "00 Index"
            @pdf_page.content += "<h2>#{doc.data['title']}</h2>\n\n"
        end
        @pdf_page.content += doc.content
    end
end

Jekyll::Hooks.register :pages, :post_init do |page| 
    if  @generate_pdf && page.data['pdf_placeholder'] == true
        STDOUT.write "Initialiaze PDF\n"
        @pdf_page = page
    end
end
