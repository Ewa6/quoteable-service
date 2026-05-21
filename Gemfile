source "https://rubygems.org"

gem "jekyll", "~> 4.2.0"
gem "base64", "~> 0.2"
gem "bigdecimal", "~> 3.2"
gem "csv", "~> 3.3"
gem "logger", "~> 1.7"
gem "minima", "~> 2.5"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

install_if -> { Gem.win_platform? && Gem::Version.new(RUBY_VERSION) < Gem::Version.new("4.0") } do
  gem "wdm", "~> 0.1.1"
end

gem "webrick", "~> 1.8"
