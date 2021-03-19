![IBM Security](./assets/IBM_Security_lockup_pos_RGB.png)
# cp4s-connector-sdk


## Use Cases 

Generating Connectors:
Cloud Pak for Security exposes connectors as a new mechanism or point of intergration for the platform. Alongside SOAR Functions, Playbooks and QRadar Apps; the CAR framework compliments the integration framework and 
this connector SDK aims to simplify the developer experience of working with Connectors.

Codegeneration is a powerful tool in a new ecosystem not only for helping to cultivate best practices among the community but also to help decrease the time to response for our users working with these tools.
Customers have to work with many many tools and ideally want to learn aas little as possible about another tool. 

For this reason we provided a best practice package someone can take and simply extend without worrying. We called this the car-reference-connector(link) and distributed it over github. The generated connector packages from this tool are based on the reference package and provide a way for a developer to streamline the bootstrapping process of getting a new connector working. 

## Installation 

### TBD - get it via Pypi : 


### Install locally
+ `git clone <url>`
+ `cd cp4s-connector-sdk`
+ `python setup.py install` 

The above will install the sdk but if you want to make changes to the SDK and see those changes on next run rather than needing to reinstall the package use the develop flag:
`python setup.py develop` 

## Usage 
### Available Commands 
#### `codegen:`
Generate boilerplate code to start developing a connector
```
connector-sdk codegen -p my_aws_connector
```
