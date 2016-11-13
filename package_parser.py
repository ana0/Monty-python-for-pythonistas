from script_parser import read_script, make_singles, make_bigrams, make_trigrams

def build_package_set():
    f = open('all_packages.txt', 'r')
    packages = set()
    for line in f:
        line = line.replace("-", "")
        line = line.replace(".", "")
        line = line.replace("_", "")
        line = line.strip()
        packages.add(line.lower())
    print "made packages"
    return packages

def check_packages(packages, singles, bigrams, trigrams):
    for package in packages:
        print "checking " + package
        if package in singles:
            record_matched_packages(package)
        if package in bigrams:
            record_matched_packages(package)
        if package in trigrams:
            record_matched_packages(package)

def record_matched_packages(package):
    f = open("matched_packages.txt", "a")
    f.write("found possible joke " + package + " \r\n")
    f.close()

tokenized_scripts = read_script()
token_set = set(make_singles(tokenized_scripts))
token_set_bigrams = set(make_bigrams(tokenized_scripts))
token_list_trigrams = set(make_trigrams(tokenized_scripts))

all_packages = build_package_set()

check_packages(all_packages, token_set, token_set_bigrams, token_list_trigrams)

