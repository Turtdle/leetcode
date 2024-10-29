def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
    if purchaseAmount % 10 < 5:
        return (10 - purchaseAmount % 10) + purchaseAmount
    return purchaseAmount - purchaseAmount % 10