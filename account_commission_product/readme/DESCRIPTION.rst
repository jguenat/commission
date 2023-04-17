This module extends the functionality of `account_commission` to allow you to
populate comission agents on invoice line by setting default agents on product.
Agents are not variant sensitive.

**IMPORTANT**: Product commission agents will be added if not already present
on the invoice line. It will not remove agents set by another method. This allows
you to have product agents in combination with partner agents.
