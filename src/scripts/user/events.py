# TODO: переписать евенты с учётом новых мини скриптов в ядре
# TODO: оформить как класс в стиле user.show_cart() user.add_to_cart()

def newUser(tg_id):
    newid = fetchMaxId("user", "id")
    newid += 1
    newInsert("user", (newid, userTgId))
    newInsert("cart", (newid, "0"))
    newInsert("favorite", (newid, "0"))

async def getCart(message, userId=False): # event
    if not userId:
        userId = await getUserId(message)
    else:
        res = fetchBySign("user", "tg_id", userId)
        userId = res[0]

    cart = fetchBySign("cart", "user_id", userId)
    products = cart[2]
    products = products.replace(',', "").split()
    return products



async def addToCart(message, product, userId=False): # event
    if not userId:
        userId = await usr.getUserTgId(message)

    actualProducts = await getCart(message, userId)
    res = ""

    for i in range(0, len(actualProducts)):
        res += str(actualProducts[i]) + ", "

    res += str(product)

    userId = fetchBySign("user", "tg_id", userId)
    userId = userId[0]

    updateRow("cart", "user_id", userId, "product_ids", res)


async def removeFromCart(message, product, userId=False): # event
    if not userId:
        userId = await usr.getUserTgId(message)

    actualProducts = await getCart(message, userId)
    actualProducts.remove(str(product))

    res = ""
    for i in range(0, len(actualProducts)):
        res += str(actualProducts[i])
        if i < len(actualProducts)-1:
            res += ", "

    userId = fetchBySign("user", "tg_id", userId)
    userId = userId[0]

    updateRow("cart", "user_id", userId, "product_ids", res)



async def getFavorites(message, userId=False): # event
    if not userId:
        userId = await getUserId(message)
    else:
        res = fetchBySign("user", "tg_id", userId)
        userId = res[0]

    cart = fetchBySign("favorite", "user_id", userId)
    products = cart[2]
    products = products.replace(',', "").split()
    return products


async def addToFavorites(message, product, userId=False): # event
    if not userId:
        userId = await getUserTgId(message)

    actualProducts = await getFavorites(message, userId)
    if str(product) in actualProducts:
        return False

    res = ""

    for i in range(0, len(actualProducts)):
        res += str(actualProducts[i]) + ", "

    res += str(product)

    userId = fetchBySign("user", "tg_id", userId)
    userId = userId[0]

    updateRow("favorite", "user_id", userId, "product_ids", res)
    return True


async def removeFromFavorites(message, product, userId=False): # event
    if not userId:
        userId = await getUserTgId(message)

    actualProducts = await getFavorites(message, userId)
    if not(str(product) in actualProducts):
        return False

    actualProducts.remove(str(product))

    res = ""
    for i in range(0, len(actualProducts)):
        res += str(actualProducts[i])
        if i < len(actualProducts)-1:
            res += ", "

    userId = fetchBySign("user", "tg_id", userId)
    userId = userId[0]

    updateRow("favorite", "user_id", userId, "product_ids", res)
    return True


def getProductUnit(message, product): # mini sc
        await removeFromCart(message, product)
        prod = fetchBySign("productunit", "product_id", product)

        if not prod:
            return False

        deleteBySign("productunit", "id", prod[0])

        return prod