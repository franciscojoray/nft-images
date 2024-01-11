from snet.sdk import SnetSDK
import segmentation_pb2
import segmentation_pb2_grpc



def invoke_service():
   snet_config = {
      "private_key": PRIVATE_KEY,
      "eth_rpc_endpoint": ETH_RPC_ENDPOINT,
      "free_call_auth_token-bin": FREE_CALL_AUTH_TOKEN_BIN,
      "free-call-token-expiry-block": FREE_CALL_TOKEN_EXPIRY_BLOCK,
      "email": EMAIL
   }
   sdk = SnetSDK(config=snet_config)
   service_client = sdk.create_service_client(
      org_id=ORG_ID,
      service_id=SERVICE_ID,
      service_stub= segmentation_pb2_grpc.SemanticSegmentationStub
   )
   with open("image.jpg", "rb") as f:
      image_content = f.read()
   request = segmentation_pb2.Request(
      img = segmentation_pb2.Image(
         mimetype = "image/jpeg",
         content = image_content
      ),
      visualise = True
   )
   response = service_client.service.segment(request)
   print(f"service invoked successfully")
   return response


response = invoke_service()