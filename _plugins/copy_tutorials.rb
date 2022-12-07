require 'fileutils'

def copy_tutorials(source, destination)
	puts %(copy_tutorials.rb: Copying tutorial files from "#{source}" to "#{destination}")
	FileUtils.cp_r source, destination
end

Jekyll::Hooks.register :site, :post_write do |jekyll|
	copy_tutorials '_includes/tutorials', '_site/tutorials'
end