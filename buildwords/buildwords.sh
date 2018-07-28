#!/bin/sh

# We start by removing all HTML tags
sed 's/<[^>]*>//g' |

# Then removing all leading spaces
sed 's/^[ \t]*//g' |

#Then we remove all empty lines
sed '/^\s*$/d' |

#Then we delete the first 5 lines, which are instructions in English
sed '1,5d' |

#Then we delete the last few lines, which are also instructions in English
sed '425,431d' |

#We only want to keep the even lines
sed '1~2d' |

#Change all ` to '
sed "s/\`/'/g" |

#Change all upper case to lower case
tr '[:upper:]' '[:lower:]' |

#Remove all words with non-hawaiian letters
sed  "/[^p^k^'^m^n^w^l^h^a^e^i^o^u]/d" |

#Finally, sort the file and remove duplicated words
sort -u 