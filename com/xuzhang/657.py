def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    movesList = list(moves)
    lstep = movesList.count("L")
    rstep = movesList.count("R")
    ustep = movesList.count("U")
    dstep = movesList.count("D")
    if lstep == rstep and ustep == dstep:
        return True
    else:
        return False


print judgeCircle("LRUDUUDD")
