from snet.sdk import SnetSDK
import config
import segmentation_pb2
import segmentation_pb2_grpc



def invoke_service():
   snet_config = {"private_key": config.PRIVATE_KEY, "eth_rpc_endpoint": config.ETH_RPC_ENDPOINT}
   sdk = SnetSDK(config=snet_config)
   service_client = sdk.create_service_client(
      org_id=config.ORG_ID,
      service_id=config.SERVICE_ID,
      service_stub= segmentation_pb2_grpc.SemanticSegmentationStub # replace service_stub
   )
   with open("image.jpg", "rb") as f:
      image_content = f.read()
   request = segmentation_pb2.Request(
      img = segmentation_pb2.Image(
         mimetype = "image/jpeg",
         content = image_content
      ),
      visualise = True
   )# replace input_method and arguments
   response = service_client.service.segment(request) # replace service_method
   print(f"service invoked successfully :: response :: {response}")


invoke_service() # call invoke service method