
from decimal import Decimal
from typing import Optional, Any
from dataclasses import dataclass
from rest_framework import serializers

from nxtbn.payment.base_payment_gateway import BasePaymentGateway, PaymentResponse

class CodPayloadSerializer(serializers.Serializer):
    """"Need to define at least a serialize, dummy as it is cod, no additional payload will come from payment gateway"""
    pass

class CashOnDelivery(BasePaymentGateway):
    """
    Implementation of a cash on delivery payment gateway.

    Cash on delivery allows customers to pay for their purchases in cash upon delivery.
    """

    def authorize(self, amount: Decimal, order_id: str, **kwargs) -> PaymentResponse:
        """
        Authorize a cash on delivery payment.

        Since cash on delivery does not require authorization beforehand,
        this method simply returns a PaymentResponse with success set to True.

        Args:
            amount (Decimal): The amount to be authorized.
            order_id (str): The unique identifier for the order.
            **kwargs: Additional keyword arguments (not used).

        Returns:
            PaymentResponse: A PaymentResponse object indicating successful authorization.
        """
        return PaymentResponse(
            success=True,
            transaction_id=None, # cash on delivery has no transaction identifier
        )

    def capture(self, amount: Decimal, order_id: str, collected: bool = False, **kwargs) -> PaymentResponse:
        """
        Capture a cash on delivery payment.

        If the cash is collected upon delivery (collected=True), the capture is successful,
        otherwise, it's unsuccessful.

        Args:
            amount (Decimal): The amount to be captured.
            order_id (str): The unique identifier for the order.
            collected (bool, optional): Whether the cash is collected upon delivery. Defaults to False.
            **kwargs: Additional keyword arguments (not used).

        Returns:
            PaymentResponse: A PaymentResponse object indicating successful or unsuccessful capture.
        """
        success = collected
        return PaymentResponse(success=success)

    def cancel(self, order_id: str, **kwargs) -> PaymentResponse:
        """
        Cancel a cash on delivery payment.

        Since cash on delivery payments are typically not cancellable,
        this method returns a PaymentResponse with success set to False.

        Args:
            order_id (str): The unique identifier for the order.
            **kwargs: Additional keyword arguments (not used).

        Returns:
            PaymentResponse: A PaymentResponse object indicating cancellation failure.
        """
        return PaymentResponse(
            success=False,
            transaction_id=None, # cash on delivery has no transaction identifier
        )

    def refund(self, amount: Decimal, order_id: str, **kwargs) -> PaymentResponse:
        """
        Refund a cash on delivery payment.

        Cash on delivery payments are typically not refundable,
        so this method returns a PaymentResponse with success set to False.

        Args:
            amount (Decimal): The amount to be refunded.
            order_id (str): The unique identifier for the order.
            **kwargs: Additional keyword arguments (not used).

        Returns:
            PaymentResponse: A PaymentResponse object indicating refund failure.
        """
        return PaymentResponse(success=False)

    def normalize_response(self, raw_response: Any) -> PaymentResponse:
        """
        Normalize raw response to a consistent PaymentResponse.

        Since cash on delivery payments do not involve external gateways,
        this method returns a PaymentResponse with success set to True
        and transaction_id set to None.

        Args:
            raw_response (Any): The raw response received (not used).

        Returns:
            PaymentResponse: A PaymentResponse object indicating success.
        """
        return PaymentResponse(success=True)

    def special_serializer(self):
        """This method will handle payload from client size will be used in api views"""
        return CodPayloadSerializer()
    
    def public_keys(self):
        return {}