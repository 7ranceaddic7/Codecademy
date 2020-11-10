highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"


def poem_blurbs(highlighted_poems):
  # what are we dealing with
  print("highlighted_poems")
  print(highlighted_poems)
  print("\n")

  # split into a list of lists
  highlighted_poems_list = highlighted_poems.split(",")

  # did we get what we expected
  print("highlighted_poems_list")
  print(highlighted_poems_list)
  print("\n")

  # clean-up highlighted_poems
  poem_list = [] 
  for each in highlighted_poems_list:
    poem_list.append(each.strip().split(":"))

  # # TEST: probe structure of poem_list (list of lists)
  # print(poem_list)

  # unpack & populate fields: author, title, year
  for item in poem_list:
    title, author, year = item

  # # TEST: each field is correctly accessed
  #  print(title, author, year)
    
    poem_blurb = "The poem {title} was published by {author} in {year}.".format(title=title, author=author, year=year)

    print(poem_blurb)

poem_blurbs(highlighted_poems)
