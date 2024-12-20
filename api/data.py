QUESTIONS_0 = [
    {
        "text": "What kind of storage is AWS S3",
        "answers": ["Object storage", "SQL database", "Block storage", "Document database"],
        "correctAnswer": 0,
    },
    {
        "text": "What does EC2 mean",
        "answers": ["Elastic Container Creator", "Elastic Compute Cloud", "Ephemeral Code Catalog", "Error Cloud 2"],
        "correctAnswer": 1,
    },
]

QUESTIONS_1 = [
    {
        "text": "What kind of storage does Amazon S3 provide?",
        "answers": ["Object storage", "SQL database", "Block storage", "Document database"],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service provides a virtual server in the cloud?",
        "answers": ["EC2", "S3", "VPC", "EBS"],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "What does EC2 stand for?",
        "answers": ["Elastic Container Creator", "Elastic Compute Cloud", "Ephemeral Code Catalog", "Error Cloud 2"],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which type of Load Balancer is designed for HTTP/HTTPS traffic and operates at Layer 7?",
        "answers": ["Network Load Balancer", "Gateway Load Balancer", "Application Load Balancer", "Classic Load Balancer"],
        "correctAnswer": 2,
        # "category": "networking"
    },
    {
        "text": "What type of database is Amazon DynamoDB?",
        "answers": ["Relational database", "Object storage", "NoSQL database", "Graph database"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "What AWS service is used to store and manage Docker container images?",
        "answers": ["EKS", "ECR", "EC2", "ELB"],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which storage class is the most cost-effective option for data that is rarely accessed?",
        "answers": ["S3 Standard", "S3 Glacier Deep Archive", "S3 Intelligent-Tiering", "S3 One Zone-IA"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which service provides a dedicated network connection from your on-premises data center to AWS?",
        "answers": ["VPN Gateway", "Direct Connect", "Internet Gateway", "VPC Peering"],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "What kind of storage solution is Amazon EBS?",
        "answers": ["Object storage", "Block storage", "File storage", "Cache storage"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service is a content delivery network (CDN) that uses edge locations to store data closer to users?",
        "answers": ["Amazon CloudFront", "Amazon Route 53", "AWS Shield", "AWS Direct Connect"],
        "correctAnswer": 0,
        # "category": "networking"
    },
    {
        "text": "Which AWS service is a NoSQL database that provides automatic scaling and serverless architecture?",
        "answers": ["Amazon Redshift", "Amazon Aurora", "Amazon DynamoDB", "Amazon RDS"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service provides an Infrastructure as Code (IaC) solution to automate resource management using YAML?",
        "answers": ["AWS CloudFormation", "AWS Beanstalk", "AWS CodeBuild", "AWS CodeDeploy"],
        "correctAnswer": 0,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "What is the purpose of AWS IAM (Identity and Access Management)?",
        "answers": ["To host virtual servers", "To create encrypted connections", "To manage user permissions", "To provide caching for applications"],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "Which AWS service allows you to monitor and set alarms for cloud resources?",
        "answers": ["AWS Config", "Amazon CloudWatch", "AWS Trusted Advisor", "AWS CloudTrail"],
        "correctAnswer": 1,
        # "category": "monitoring and analytics"
    },
    {
        "text": "What is the difference between a Network ACL and a Security Group in AWS?",
        "answers": [
            "Network ACL is stateful, Security Group is stateless",
            "Security Group is stateful, Network ACL is stateless",
            "Both are stateful",
            "Both are stateless"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which service provides automatic DDoS protection for AWS applications?",
        "answers": ["AWS WAF", "AWS Shield", "Amazon CloudFront", "AWS KMS"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service is used to audit and track user activity in an AWS account?",
        "answers": ["AWS CloudTrail", "Amazon Inspector", "AWS Trusted Advisor", "Amazon GuardDuty"],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "What service would you use for a scalable, fully managed data warehouse on AWS?",
        "answers": ["Amazon RDS", "Amazon Redshift", "Amazon DynamoDB", "Amazon DocumentDB"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service allows you to manage multiple AWS accounts under a single organization?",
        "answers": ["AWS IAM", "AWS Organizations", "AWS Directory Service", "AWS CloudTrail"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "What does the AWS Free Tier offer for new users?",
        "answers": [
            "Always free usage of EC2 and S3",
            "Free usage for 12 months with usage limits",
            "Unlimited free usage of all AWS services",
            "Pay-as-you-go usage only after the first month"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    }
]

QUESTIONS_2 = [
    {
        "text": "Which service is a managed NoSQL database that supports both key-value and document data models?",
        "answers": ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon ElastiCache"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS database service is optimized for online analytical processing (OLAP) and large-scale data warehousing?",
        "answers": ["Amazon RDS", "Amazon Redshift", "Amazon DynamoDB", "Amazon Aurora"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "In AWS, which type of storage is attached directly to an EC2 instance and terminates along with the instance?",
        "answers": ["S3", "EFS", "Instance store", "EBS"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Which of the following is a serverless, managed compute service for containers?",
        "answers": ["Amazon ECS", "AWS Fargate", "Amazon ECR", "Amazon EC2"],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which AWS service provides automatic scaling and high availability for a managed relational database?",
        "answers": ["Amazon DynamoDB", "Amazon RDS", "Amazon ElastiCache", "Amazon Redshift"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "For managing DNS services in AWS, which service should you use?",
        "answers": ["Amazon CloudFront", "Amazon Route 53", "AWS Direct Connect", "AWS IAM"],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "What is the main purpose of Amazon VPC (Virtual Private Cloud)?",
        "answers": [
            "To provide object storage",
            "To securely isolate and control network traffic in the cloud",
            "To create an automatic backup solution",
            "To monitor cloud resources"
        ],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "In a VPC, which component allows direct access to the internet for resources inside a VPC?",
        "answers": ["NAT Gateway", "Internet Gateway", "Virtual Private Gateway", "Direct Connect"],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "Which AWS service is used for real-time threat detection using machine learning and network activity analysis?",
        "answers": ["AWS Shield", "Amazon Inspector", "AWS WAF", "Amazon GuardDuty"],
        "correctAnswer": 3,
        # "category": "security"
    },
    {
        "text": "What AWS service allows you to automate the creation and deployment of resources using code?",
        "answers": ["AWS CloudFormation", "AWS Elastic Beanstalk", "AWS CodeBuild", "Amazon EKS"],
        "correctAnswer": 0,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which service would you use to monitor and analyze logs in your AWS environment?",
        "answers": ["Amazon CloudWatch", "AWS Trusted Advisor", "AWS Config", "AWS Cost Explorer"],
        "correctAnswer": 0,
        # "category": "monitoring and analytics"
    },
    {
        "text": "Which AWS database service provides a graph database for applications requiring highly connected data?",
        "answers": ["Amazon DynamoDB", "Amazon Neptune", "Amazon RDS", "Amazon ElastiCache"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What type of firewall is AWS Security Groups classified as?",
        "answers": ["Stateless at the subnet level", "Stateful at the instance level", "Stateful at the subnet level", "Stateless at the instance level"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS database service offers a ledger database designed for immutable records and compliance use cases?",
        "answers": ["Amazon DynamoDB", "Amazon RDS", "Amazon QLDB", "Amazon Redshift"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Which service is a fully managed container orchestration platform that allows you to run Kubernetes on AWS?",
        "answers": ["AWS Fargate", "Amazon ECS", "Amazon EKS", "AWS Lambda"],
        "correctAnswer": 2,
        # "category": "compute"
    },
    {
        "text": "Which AWS tool allows you to estimate costs and create budgeting alerts for resource usage?",
        "answers": ["AWS Trusted Advisor", "AWS Budgets", "AWS Cost Explorer", "AWS Pricing Calculator"],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which service would you use to establish a private and dedicated connection between your data center and an AWS VPC?",
        "answers": ["AWS VPN", "AWS Direct Connect", "Internet Gateway", "NAT Gateway"],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "Which storage solution is designed for highly durable storage of infrequently accessed data at a low cost?",
        "answers": ["Amazon S3 Standard", "Amazon S3 Glacier", "Amazon EFS", "Amazon RDS"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What is the purpose of Amazon CloudFront in AWS?",
        "answers": [
            "To run virtual servers",
            "To store data in a scalable way",
            "To deliver content with low latency from edge locations",
            "To monitor application performance"
        ],
        "correctAnswer": 2,
        # "category": "networking"
    },
    {
        "text": "Which AWS service is used to automatically optimize the storage tier of your data based on usage patterns?",
        "answers": ["Amazon S3 Standard", "Amazon EBS", "S3 Intelligent-Tiering", "Amazon Glacier"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "What is the default maximum number of member accounts in an AWS Organization?",
        "answers": ["2", "4", "10", "50"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service is primarily used to run machine learning models without managing infrastructure?",
        "answers": ["Amazon EC2", "AWS Lambda", "Amazon SageMaker", "AWS Fargate"],
        "correctAnswer": 2,
        # "category": "innovation"
    },
    {
        "text": "Which AWS database is optimized for massive amounts of structured data that can be queried efficiently across columns?",
        "answers": ["Amazon DynamoDB", "Amazon RDS", "Amazon Redshift", "Amazon ElastiCache"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS tool offers automated security assessment recommendations to improve your security posture?",
        "answers": ["AWS Shield", "Amazon Inspector", "AWS Trusted Advisor", "Amazon CloudWatch"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "For high performance and low latency TCP traffic, which load balancer is most suitable?",
        "answers": ["Application Load Balancer", "Classic Load Balancer", "Network Load Balancer", "Gateway Load Balancer"],
        "correctAnswer": 2,
        # "category": "networking"
    },
    {
        "text": "What AWS service provides audit trails for all API requests made to AWS resources?",
        "answers": ["AWS IAM", "AWS CloudTrail", "Amazon GuardDuty", "AWS Config"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS feature is essential for controlling costs and usage across multiple accounts within an organization?",
        "answers": ["AWS Budgets", "Consolidated Billing", "AWS Trusted Advisor", "AWS Cost Explorer"],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service offers machine learning-powered text extraction from scanned documents?",
        "answers": ["Amazon SageMaker", "Amazon Comprehend", "Amazon Textract", "Amazon Transcribe"],
        "correctAnswer": 2,
        # "category": "innovation"
    },
    {
        "text": "What AWS service allows for web application firewall rules to filter and protect traffic?",
        "answers": ["AWS Shield", "AWS WAF", "Amazon CloudFront", "AWS IAM"],
        "correctAnswer": 1,
        # "category": "security"
    }
]

QUESTIONS_3 = [
    {
        "text": "What AWS service provides a fully managed message queue service that allows decoupling of microservices and distributed systems?",
        "answers": ["Amazon SQS", "Amazon SNS", "AWS Step Functions", "AWS AppSync"],
        "correctAnswer": 0,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS service provides access control by allowing you to manage users, groups, and roles with policies?",
        "answers": ["AWS CloudTrail", "Amazon IAM", "AWS Config", "AWS KMS"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which storage service is ideal for storing and archiving infrequently accessed data at a very low cost?",
        "answers": ["Amazon S3 Standard", "Amazon Glacier", "Amazon EFS", "Amazon RDS"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What is the purpose of AWS Direct Connect?",
        "answers": [
            "To manage security groups",
            "To connect multiple AWS accounts",
            "To establish a private connection between AWS and your data center",
            "To replicate data across regions"
        ],
        "correctAnswer": 2,
        # "category": "networking"
    },
    {
        "text": "Which AWS tool helps you optimize costs, security, and performance by providing best-practice recommendations?",
        "answers": ["AWS Trusted Advisor", "Amazon GuardDuty", "AWS Artifact", "AWS Security Hub"],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service should you use for automating deployments and scaling applications hosted on EC2 without managing the underlying infrastructure?",
        "answers": ["AWS CloudFormation", "AWS Elastic Beanstalk", "AWS Lambda", "Amazon EKS"],
        "correctAnswer": 1,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS service allows you to build conversational chatbots and voice interfaces using AI?",
        "answers": ["Amazon Lex", "Amazon SageMaker", "AWS Lambda", "AWS IoT"],
        "correctAnswer": 0,
        # "category": "innovation"
    },
    {
        "text": "Which AWS feature allows you to receive compliance reports and white papers to help you verify security and compliance?",
        "answers": ["AWS Shield", "AWS Artifact", "AWS Trusted Advisor", "AWS CloudTrail"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "What type of storage is Amazon Elastic File System (EFS) designed for?",
        "answers": [
            "Infrequent Access",
            "Object storage",
            "Shared storage across multiple EC2 instances",
            "Backup storage for S3"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service lets you create an isolated network within the AWS cloud for your resources?",
        "answers": ["Amazon VPC", "AWS Direct Connect", "AWS Organizations", "Amazon CloudFront"],
        "correctAnswer": 0,
        # "category": "networking"
    },
    {
        "text": "What AWS service would you use to monitor application metrics, set alarms, and trigger actions based on thresholds?",
        "answers": ["AWS Trusted Advisor", "Amazon CloudWatch", "AWS Config", "Amazon GuardDuty"],
        "correctAnswer": 1,
        # "category": "monitoring and analytics"
    },
    {
        "text": "For migrating a database to AWS, which service can help perform the migration with minimal downtime?",
        "answers": ["AWS Data Pipeline", "AWS Database Migration Service (DMS)", "Amazon Redshift", "AWS Glue"],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Which of the following AWS services is a content delivery network (CDN) that delivers content with low latency?",
        "answers": ["Amazon CloudFront", "AWS Route 53", "Amazon S3", "AWS Direct Connect"],
        "correctAnswer": 0,
        # "category": "networking"
    },
    {
        "text": "What service can you use to protect web applications from common security threats like SQL injection and cross-site scripting?",
        "answers": ["Amazon GuardDuty", "AWS Shield", "AWS WAF", "AWS Security Hub"],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "Which AWS service is designed for distributed ledger applications requiring an immutable, cryptographically verifiable transaction log?",
        "answers": ["Amazon DynamoDB", "Amazon QLDB", "Amazon RDS", "Amazon ElastiCache"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What AWS service provides fully managed data warehousing and is optimized for complex queries and analytics?",
        "answers": ["Amazon DynamoDB", "Amazon Redshift", "Amazon S3", "Amazon RDS"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What does AWS use to manage and limit access permissions within accounts, including permissions for member accounts in an organization?",
        "answers": ["AWS IAM", "Service Control Policies (SCP)", "AWS KMS", "AWS WAF"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service provides a scalable document database that is fully managed and supports MongoDB workloads?",
        "answers": ["Amazon DocumentDB", "Amazon Neptune", "Amazon RDS", "Amazon DynamoDB"],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service is a fully managed, highly scalable data warehousing service designed for large-scale analytics?",
        "answers": ["Amazon RDS", "Amazon Redshift", "Amazon DynamoDB", "AWS Glue"],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "In which AWS support plan do you get a designated Technical Account Manager (TAM) with 24/7 access to technical support?",
        "answers": ["Basic", "Developer", "Business", "Enterprise"],
        "correctAnswer": 3,
        # "category": "pricing and support"
    },
    {
        "text": "What AWS service provides monitoring and logging for compliance and auditing by recording API calls?",
        "answers": ["AWS IAM", "Amazon CloudWatch", "AWS CloudTrail", "AWS Config"],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "What AWS service is a fully managed caching solution that supports both Memcached and Redis engines?",
        "answers": ["Amazon DynamoDB", "Amazon RDS", "Amazon ElastiCache", "Amazon Redshift"],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service allows you to analyze text for insights and identify language, key phrases, and sentiment?",
        "answers": ["Amazon Lex", "Amazon Comprehend", "Amazon Textract", "Amazon Translate"],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "What AWS service allows you to implement machine learning models using reinforcement learning with an autonomous race car?",
        "answers": ["Amazon SageMaker", "AWS DeepRacer", "AWS Ground Station", "Amazon Comprehend"],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "Which service provides secure, private network access between AWS and your on-premises network without using the internet?",
        "answers": ["Internet Gateway", "NAT Gateway", "AWS Direct Connect", "AWS VPN"],
        "correctAnswer": 2,
        # "category": "networking"
    },
    {
        "text": "What AWS tool provides a unified dashboard that aggregates security alerts from multiple services, helping you assess security posture?",
        "answers": ["AWS WAF", "AWS Security Hub", "AWS Trusted Advisor", "AWS Artifact"],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service is used to launch virtual servers and provides resizable compute capacity in the cloud?",
        "answers": ["Amazon ECS", "Amazon EKS", "Amazon EC2", "AWS Fargate"],
        "correctAnswer": 2,
        # "category": "compute"
    },
    {
        "text": "For storing and managing Docker container images, which AWS service would you use?",
        "answers": ["Amazon ECR", "Amazon S3", "AWS Fargate", "AWS Lambda"],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "What AWS service provides centralized logging for compliance and auditing across multiple AWS accounts and services?",
        "answers": ["AWS IAM", "AWS Trusted Advisor", "AWS CloudTrail", "Amazon CloudWatch"],
        "correctAnswer": 2,
        # "category": "security"
    },
]

QUESTIONS_4 = [
    {
        "text": "Which AWS service allows for identity federation, enabling users to access AWS resources using credentials from external identity providers?",
        "answers": ["Amazon IAM", "AWS SSO", "Amazon Cognito", "AWS Organizations"],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "What is the purpose of AWS Cloud Adoption Framework (CAF)?",
        "answers": [
            "To assess and plan a migration to AWS",
            "To manage billing and cost allocation",
            "To help architect serverless applications",
            "To provide support for high-performance computing"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which of the following is NOT one of the six strategies for migration in the AWS Cloud Adoption Framework (CAF)?",
        "answers": ["Rehosting", "Replatforming", "Refactoring", "Rewriting"],
        "correctAnswer": 3,
        # "category": "migration and innovation"
    },
    {
        "text": "What AWS tool allows you to break down costs by service and usage to help understand where your spend is going?",
        "answers": ["AWS Cost Explorer", "AWS Budget", "AWS Trusted Advisor", "AWS Pricing Calculator"],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which tool can be used to create cost alerts when spending exceeds a specified threshold in your AWS account?",
        "answers": ["AWS Budget", "AWS Cost Explorer", "AWS Pricing Calculator", "AWS Cost Optimization"],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS ML service allows you to build and deploy machine learning models without extensive ML experience?",
        "answers": ["Amazon SageMaker", "Amazon Comprehend", "AWS Lex", "Amazon Transcribe"],
        "correctAnswer": 0,
        # "category": "innovation"
    },
    {
        "text": "What is Amazon Textract used for in AWS?",
        "answers": [
            "Analyzing customer sentiment in text data",
            "Extracting text from scanned documents",
            "Generating synthetic data for ML models",
            "Analyzing text for language patterns"
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "Which AWS migration strategy is also known as 'lift and shift'?",
        "answers": ["Rehosting", "Repurchasing", "Refactoring", "Rearchitecting"],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS migration strategy involves moving applications to the cloud with minimal modification to leverage cloud benefits?",
        "answers": ["Refactoring", "Rehosting", "Replatforming", "Retiring"],
        "correctAnswer": 2,
        # "category": "migration and innovation"
    },
    {
        "text": "What does MTTR stand for in the context of cloud infrastructure monitoring?",
        "answers": [
            "Mean Time to Resolution",
            "Monthly Time to Repair",
            "Mean Total Task Response",
            "Monthly Technical Tracking Report"
        ],
        "correctAnswer": 0,
        # "category": "monitoring and analytics"
    },
    {
        "text": "AWS's Total Cost of Ownership (TCO) Calculator helps you understand:",
        "answers": [
            "Estimated monthly AWS bills",
            "Cost of current on-premises infrastructure compared to AWS",
            "Pricing details of individual AWS services",
            "Support plan costs for enterprise customers"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS AI service would you use to automatically transcribe audio files into text?",
        "answers": ["Amazon Lex", "Amazon Transcribe", "Amazon Polly", "Amazon Comprehend"],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "Which of the following is an advantage of cloud computing?",
        "answers": [
            "Increased up-front costs",
            "Dedicated physical servers",
            "Ability to stop guessing capacity needs",
            "Requirement to manually update all software"
        ],
        "correctAnswer": 2,
        # "category": "general cloud computing concepts"
    },
    {
        "text": "What benefit does AWS Snowball provide?",
        "answers": [
            "Hosting data-intensive applications in the cloud",
            "Securely transferring large volumes of data into AWS",
            "Analyzing data in real-time",
            "Providing on-demand GPU compute power"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "What is Amazon Polly used for?",
        "answers": [
            "Natural language processing",
            "Speech-to-text transcription",
            "Text-to-speech conversion",
            "Sentiment analysis"
        ],
        "correctAnswer": 2,
        # "category": "innovation"
    },
    {
        "text": "In AWS, what is the default response time for Business-level support plans?",
        "answers": [
            "15 minutes",
            "1 hour",
            "24 hours",
            "12 hours"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "What is the AWS Ground Station service used for?",
        "answers": [
            "Running machine learning models",
            "Deploying satellite communication solutions",
            "Managing database migrations",
            "Setting up ground-level security networks"
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "Which AWS service would you use to test your infrastructure against security best practices and find security vulnerabilities?",
        "answers": ["AWS Inspector", "AWS Trusted Advisor", "AWS Security Hub", "AWS CloudTrail"],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "Amazon DynamoDB Accelerator (DAX) is primarily used to:",
        "answers": [
            "Backup DynamoDB tables",
            "Add caching for DynamoDB to improve response times",
            "Run SQL queries on DynamoDB data",
            "Migrate data from RDS to DynamoDB"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What AWS support plan provides 15-minute response times for business-critical issues?",
        "answers": ["Enterprise", "Developer", "Business", "Basic"],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS AI service would you use to detect fraud in real-time transactions?",
        "answers": ["Amazon Comprehend", "Amazon Fraud Detector", "Amazon Lex", "AWS GuardDuty"],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "What AWS tool provides guidance for cost management and helps identify opportunities to reduce costs across your AWS environment?",
        "answers": ["AWS Trusted Advisor", "AWS Cost Explorer", "AWS Budgets", "AWS Pricing Calculator"],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service allows you to securely store and manage encryption keys?",
        "answers": ["AWS Secrets Manager", "AWS CloudTrail", "AWS Key Management Service (KMS)", "AWS Shield"],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "Which AWS machine learning service helps analyze patterns in text data and offers features like sentiment analysis and language detection?",
        "answers": ["Amazon Textract", "Amazon Comprehend", "Amazon Translate", "Amazon Polly"],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "What AWS resource management tool allows you to define infrastructure as code using JSON or YAML templates?",
        "answers": ["AWS CloudFormation", "AWS Config", "AWS Systems Manager", "AWS CodeBuild"],
        "correctAnswer": 0,
        # "category": "infrastructure and reliability"
    },
]


QUESTIONS_5 = [
    {
        "text": "What is AWS Artifact used for?",
        "answers": [
            "To generate compliance reports and certifications",
            "To monitor infrastructure performance",
            "To automate deployment processes",
            "To provide machine learning insights on stored data"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "Which AWS service provides DDoS protection and helps secure applications from web threats using web ACLs?",
        "answers": ["AWS WAF", "AWS GuardDuty", "AWS Shield", "AWS Firewall Manager"],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "In AWS Organizations, what is the purpose of Service Control Policies (SCPs)?",
        "answers": [
            "To encrypt data across multiple accounts",
            "To restrict AWS service permissions across accounts",
            "To monitor costs across multiple AWS accounts",
            "To enable automated scaling for applications"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "What are Organizational Units (OUs) in AWS Organizations used for?",
        "answers": [
            "Grouping services by region",
            "Grouping accounts for hierarchical management",
            "Grouping data across multiple storage types",
            "Grouping EC2 instances within a VPC"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which of the following is NOT a pillar of the AWS Well-Architected Framework?",
        "answers": [
            "Operational Excellence",
            "Cost Optimization",
            "Sustainability",
            "System Administration"
        ],
        "correctAnswer": 3,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS service is designed for building autonomous driving models using a scale model race car?",
        "answers": ["Amazon DeepRacer", "AWS RoboMaker", "Amazon Lex", "AWS CodeBuild"],
        "correctAnswer": 0,
        # "category": "innovation"
    },
    {
        "text": "AWS Ground Station is a service that allows users to:",
        "answers": [
            "Host virtual private cloud environments",
            "Create and manage satellite communications",
            "Analyze streaming video data",
            "Build and train machine learning models"
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "Which AWS service is designed to scan and assess applications for security vulnerabilities and best practices?",
        "answers": [
            "AWS Security Hub",
            "AWS Inspector",
            "AWS Trusted Advisor",
            "AWS Config"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "What benefit does using Organizational Units (OUs) in AWS Organizations provide?",
        "answers": [
            "Faster network performance",
            "Cost reduction for large accounts",
            "Simplified management of policies across accounts",
            "Automatic scaling of resources across accounts"
        ],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "In AWS Shield Advanced, what additional protections are offered beyond Shield Standard?",
        "answers": [
            "Protection from all web-based attacks",
            "Increased DDoS protection and access to a dedicated response team",
            "AI-based real-time threat detection",
            "Built-in encryption for all data at rest"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "AWS WAF (Web Application Firewall) uses which type of rule to block or allow web traffic?",
        "answers": [
            "Role-based policies",
            "Network access control lists",
            "Security groups",
            "Web ACL rules"
        ],
        "correctAnswer": 3,
        # "category": "security"
    },
    {
        "text": "What is the purpose of Amazon DocumentDB?",
        "answers": [
            "To provide a highly scalable key-value database",
            "To offer a managed graph database service",
            "To manage MongoDB-compatible document databases",
            "To store data for machine learning applications"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "Amazon Neptune is a managed database service designed for:",
        "answers": [
            "Document storage",
            "Graph data",
            "Text analysis",
            "Data warehousing"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS database service is ideal for big data analytics and data warehousing?",
        "answers": [
            "Amazon RDS",
            "Amazon Aurora",
            "Amazon Redshift",
            "Amazon DocumentDB"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "AWS Organizations allows you to manage multiple AWS accounts. By default, what is the maximum number of accounts allowed per organization?",
        "answers": ["4", "10", "100", "20"],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "What AWS service helps users ensure they are following the best practices for building secure and resilient cloud applications?",
        "answers": [
            "AWS CloudTrail",
            "AWS Trusted Advisor",
            "AWS Well-Architected Tool",
            "AWS Config"
        ],
        "correctAnswer": 2,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS service allows for automated checks against AWS security best practices and compliance frameworks?",
        "answers": [
            "AWS Config",
            "AWS Artifact",
            "AWS Trusted Advisor",
            "AWS Security Hub"
        ],
        "correctAnswer": 3,
        # "category": "security"
    },
]

QUESTIONS_6 = [
    {
        "text": "What purpose does AWS Artifact serve in an organization's compliance efforts?",
        "answers": [
            "Provides compliance reports and certifications for auditing",
            "Monitors compliance of AWS resources in real-time",
            "Automates encryption for all stored data",
            "Alerts administrators to security vulnerabilities"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "Which AWS service helps migrate large data sets to the cloud by physically shipping devices to AWS?",
        "answers": [
            "AWS Direct Connect",
            "AWS Migration Hub",
            "AWS Snowball",
            "AWS DataSync"
        ],
        "correctAnswer": 2,
        # "category": "migration and innovation"
    },
    {
        "text": "What is the maximum data storage capacity for the AWS Snowmobile data migration device?",
        "answers": [
            "80 TB",
            "1 PB",
            "100 PB",
            "1 EB"
        ],
        "correctAnswer": 2,
        # "category": "migration and innovation"
    },
    {
        "text": "AWS Key Management Service (KMS) is primarily used for:",
        "answers": [
            "Monitoring AWS resources",
            "Managing and creating encryption keys",
            "Managing identity and access permissions",
            "Optimizing storage costs"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "What feature of AWS IAM helps improve account security by requiring users to provide two forms of authentication?",
        "answers": [
            "Access keys",
            "Multi-Factor Authentication (MFA)",
            "IAM policies",
            "Security groups"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service can automatically monitor and detect unusual activity across AWS resources?",
        "answers": [
            "AWS Config",
            "AWS CloudWatch",
            "AWS GuardDuty",
            "AWS Inspector"
        ],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "Which migration strategy is best described as 'moving an application as-is' to AWS without major changes?",
        "answers": [
            "Refactoring",
            "Rehosting",
            "Repurchasing",
            "Replatforming"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Amazon Quantum Ledger Database (QLDB) is best suited for applications requiring:",
        "answers": [
            "Mutable data for dynamic records",
            "Immutable data storage with an append-only ledger",
            "Graph data storage",
            "Temporary, high-throughput storage"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "AWS Trusted Advisor provides recommendations across which of the following areas?",
        "answers": [
            "Cost optimization, security, performance, fault tolerance, and service limits",
            "Storage efficiency, compute efficiency, and network resilience",
            "Encryption and compliance audits",
            "Machine learning model training and evaluation"
        ],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS identity feature allows users to log in with credentials from an external identity provider, such as Google or Facebook?",
        "answers": [
            "Identity Federation",
            "IAM Roles",
            "Cross-account access",
            "AWS Organizations"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "What type of AWS database is Amazon Neptune best suited for?",
        "answers": [
            "Document-based data",
            "Graph-based data",
            "Relational data",
            "Columnar data"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What is the main purpose of the AWS Well-Architected Tool?",
        "answers": [
            "Providing compliance reports for security audits",
            "Guiding users in applying AWS best practices for cloud architectures",
            "Optimizing the cost of AWS resources",
            "Setting up automated security rules"
        ],
        "correctAnswer": 1,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "What AWS service assists in consolidating and managing multiple AWS accounts within an organization?",
        "answers": [
            "AWS Identity and Access Management (IAM)",
            "AWS Artifact",
            "AWS Organizations",
            "AWS Trusted Advisor"
        ],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "Which service provides edge-based content caching to improve performance for global users?",
        "answers": [
            "AWS Direct Connect",
            "Amazon Route 53",
            "Amazon CloudFront",
            "AWS Storage Gateway"
        ],
        "correctAnswer": 2,
        # "category": "networking"
    },
    {
        "text": "Amazon Augmented AI (A2I) is primarily used to:",
        "answers": [
            "Translate text to other languages",
            "Run automated machine learning models",
            "Add human reviews to machine learning workflows",
            "Provide voice-based services to applications"
        ],
        "correctAnswer": 2,
        # "category": "innovation"
    },
    {
        "text": "AWS CloudTrail primarily helps organizations with:",
        "answers": [
            "Logging and tracking user and API activity",
            "Creating a private network in the cloud",
            "Setting up and deploying machine learning models",
            "Controlling access to AWS resources"
        ],
        "correctAnswer": 0,
        # "category": "monitoring and analytics"
    },
    {
        "text": "Which AWS service provides automatic distribution of traffic across multiple instances for improved availability?",
        "answers": [
            "AWS Auto Scaling",
            "Amazon CloudFront",
            "AWS Elastic Load Balancing",
            "Amazon Route 53"
        ],
        "correctAnswer": 2,
        # "category": "networking"
    }
]


QUESTIONS_7 = [
    {
        "text": "Which AWS service allows you to set custom alerts based on cost and usage thresholds?",
        "answers": [
            "AWS Billing",
            "AWS Cost Explorer",
            "AWS Budgets",
            "AWS Trusted Advisor"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "What is the purpose of AWS Identity and Access Management (IAM) policies?",
        "answers": [
            "They provide a central place to manage costs across multiple AWS accounts.",
            "They define permissions for users, groups, and roles to access AWS resources.",
            "They automate the deployment of applications on AWS infrastructure.",
            "They optimize the security of AWS applications by enforcing firewall rules."
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service is primarily used to run queries on large datasets in Amazon S3 without needing to move the data?",
        "answers": [
            "AWS Glue",
            "Amazon Redshift",
            "Amazon Athena",
            "Amazon RDS"
        ],
        "correctAnswer": 2,
        # "category": "analytics"
    },
    {
        "text": "What does Amazon Comprehend enable you to do?",
        "answers": [
            "Translate text into different languages",
            "Understand relationships and patterns in text using natural language processing",
            "Generate recommendations based on user behavior",
            "Analyze real-time network traffic for security threats"
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "What is the role of AWS Direct Connect in an AWS environment?",
        "answers": [
            "Providing a VPN for secure remote access",
            "Setting up a private connection between your on-premises data center and AWS",
            "Automatically distributing incoming application traffic across multiple targets",
            "Monitoring application performance in real time"
        ],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "Which AWS service can help you monitor application metrics and set alarms based on performance thresholds?",
        "answers": [
            "AWS CloudTrail",
            "AWS CloudFormation",
            "Amazon CloudWatch",
            "AWS Config"
        ],
        "correctAnswer": 2,
        # "category": "monitoring and analytics"
    },
    {
        "text": "Which AWS service is included in the Always Free Tier and provides up to 1 million invocations per month?",
        "answers": [
            "AWS Lambda",
            "Amazon EC2",
            "Amazon S3",
            "Amazon RDS"
        ],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Amazon Fraud Detector is designed to:",
        "answers": [
            "Monitor and protect against DDoS attacks",
            "Automatically detect fraudulent activity using machine learning",
            "Translate text in multiple languages",
            "Help build and manage machine learning models"
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "What benefit does using Amazon SageMaker provide for machine learning (ML) projects?",
        "answers": [
            "It automatically encrypts all data at rest.",
            "It allows building, training, and deploying ML models at scale.",
            "It provides an immutable database ledger for secure records.",
            "It provides a free database for document-based storage."
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "In AWS, what does the Well-Architected Framework pillar 'Reliability' emphasize?",
        "answers": [
            "Optimizing costs by reducing resource use",
            "Enabling systems to recover from failures and meet business continuity goals",
            "Implementing encryption to protect data integrity",
            "Improving application performance with faster load times"
        ],
        "correctAnswer": 1,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS support plan includes a dedicated Technical Account Manager (TAM) and 15-minute response times for critical issues?",
        "answers": [
            "Basic",
            "Developer",
            "Business",
            "Enterprise"
        ],
        "correctAnswer": 3,
        # "category": "pricing and support"
    },
    {
        "text": "Which free AWS service helps you audit and track changes to your AWS infrastructure over time?",
        "answers": [
            "AWS Trusted Advisor",
            "AWS CloudTrail",
            "AWS Config",
            "AWS Shield"
        ],
        "correctAnswer": 1,
        # "category": "monitoring and analytics"
    },
    {
        "text": "Amazon Textract is primarily used for:",
        "answers": [
            "Translating text into different languages",
            "Analyzing network traffic for threats",
            "Extracting text and data from scanned documents",
            "Building conversational interfaces with voice and text"
        ],
        "correctAnswer": 2,
        # "category": "innovation"
    },
    {
        "text": "What is the primary use of Amazon Route 53 in an AWS environment?",
        "answers": [
            "Connecting private networks",
            "Managing DNS web service for domain routing",
            "Distributing content globally",
            "Configuring security groups for EC2 instances"
        ],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "What is the main purpose of AWS Organizations?",
        "answers": [
            "Setting security groups for instances",
            "Managing multiple AWS accounts under a central organization",
            "Automating resource deployments",
            "Providing DDoS protection to applications"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "What kind of support does the AWS Basic Support Plan offer?",
        "answers": [
            "24/7 phone access to AWS Support Engineers",
            "Access to AWS Trusted Advisor core checks and AWS Personal Health Dashboard",
            "Dedicated Technical Account Manager (TAM)",
            "Priority access to AWS infrastructure during high-demand events"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    }
]

QUESTIONS_8 = [
    {
        "text": "Which S3 storage class is designed for data that is rarely accessed but requires rapid retrieval when needed?",
        "answers": [
            "S3 Standard",
            "S3 Intelligent-Tiering",
            "S3 Glacier Instant Retrieval",
            "S3 Glacier Deep Archive"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "What is the AWS Database Migration Service (DMS) primarily used for?",
        "answers": [
            "Setting up relational databases in the cloud",
            "Migrating and replicating databases between on-premises and AWS environments",
            "Backing up data to Amazon S3",
            "Analyzing large datasets using machine learning"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "According to the AWS Well-Architected Framework, which pillar focuses on optimizing your architecture for costs and reducing unnecessary resources?",
        "answers": [
            "Reliability",
            "Cost Optimization",
            "Operational Excellence",
            "Performance Efficiency"
        ],
        "correctAnswer": 1,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS service helps developers build and deploy conversational interfaces using voice and text?",
        "answers": [
            "Amazon Lex",
            "Amazon Textract",
            "Amazon Comprehend",
            "AWS DeepLens"
        ],
        "correctAnswer": 0,
        # "category": "innovation"
    },
    {
        "text": "What is Amazon Ground Station used for?",
        "answers": [
            "Developing autonomous driving models",
            "Hosting and running satellite communications operations",
            "Performing data warehousing",
            "Managing VPN connections to private networks"
        ],
        "correctAnswer": 1,
        # "category": "innovation"
    },
    {
        "text": "Which AWS migration strategy involves moving applications without any code modification to AWS infrastructure?",
        "answers": [
            "Rehosting",
            "Replatforming",
            "Refactoring",
            "Repurchasing"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "What is Amazon Neptune best suited for?",
        "answers": [
            "Relational databases",
            "Graph databases",
            "Key-value stores",
            "Data warehousing"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which of the following is an advantage of the AWS cloud over traditional data centers?",
        "answers": [
            "Higher upfront capital costs",
            "Predictable fixed capacity",
            "Massive economies of scale",
            "Increased management overhead"
        ],
        "correctAnswer": 2,
        # "category": "cloud advantages"
    },
    {
        "text": "What is Amazon QLDB (Quantum Ledger Database) used for?",
        "answers": [
            "Data analysis and visualization",
            "Managing cryptographic keys",
            "Storing data with an immutable transaction log",
            "Running machine learning models at scale"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "In AWS Organizations, what is the purpose of service control policies (SCPs)?",
        "answers": [
            "To automatically back up AWS resources",
            "To restrict or allow access to specific AWS services across member accounts",
            "To enforce encryption of all data in transit",
            "To monitor and log API calls to AWS resources"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service provides recommendations for cost optimization, security, performance, and fault tolerance?",
        "answers": [
            "AWS Config",
            "AWS Trusted Advisor",
            "AWS Shield",
            "AWS Key Management Service (KMS)"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service provides an on-premises solution for running AWS services inside your own data center?",
        "answers": [
            "AWS Outposts",
            "AWS Direct Connect",
            "Amazon VPC",
            "AWS Snowball"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "What is the purpose of Amazon Elastic File System (EFS)?",
        "answers": [
            "To provide scalable file storage that can be shared across multiple EC2 instances",
            "To offer long-term archival storage with infrequent access",
            "To store Docker images for containerized applications",
            "To store key-value pairs for DynamoDB databases"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    }
]


QUESTIONS_9 = [
    {
        "text": "Which AWS service allows you to provision a dedicated, low-latency network connection between your on-premises data center and AWS?",
        "answers": [
            "AWS Direct Connect",
            "Amazon VPC Peering",
            "AWS VPN Gateway",
            "Amazon Route 53"
        ],
        "correctAnswer": 0,
        # "category": "networking"
    },
    {
        "text": "Which of the following describes AWS Elastic Beanstalk?",
        "answers": [
            "A platform as a service (PaaS) for managing and deploying applications",
            "A serverless compute engine for containers",
            "An Infrastructure as a Service (IaaS) for EC2 instances",
            "A managed service for database backups"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "Which AWS service can be used to automate the deployment of infrastructure using code in YAML or JSON format?",
        "answers": [
            "AWS CloudFormation",
            "AWS Elastic Beanstalk",
            "AWS Lambda",
            "Amazon EC2 Auto Scaling"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "What is the main benefit of using Amazon S3 Glacier Deep Archive for storage?",
        "answers": [
            "High performance for frequently accessed data",
            "Low-cost, long-term archival storage with retrieval times in hours",
            "Optimized for real-time big data analytics",
            "Instant retrieval of archival data"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service can automatically adjust the number of EC2 instances based on traffic demand?",
        "answers": [
            "AWS Lambda",
            "Amazon EC2 Auto Scaling",
            "Amazon Elastic Load Balancer",
            "AWS Elastic Beanstalk"
        ],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which of the following is a managed blockchain service in AWS?",
        "answers": [
            "Amazon Aurora",
            "Amazon ElastiCache",
            "Amazon Managed Blockchain",
            "Amazon Redshift"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "What is the primary purpose of AWS Identity and Access Management (IAM)?",
        "answers": [
            "To manage DNS records for domains",
            "To configure and manage network traffic",
            "To securely control access to AWS resources",
            "To automate EC2 instance scaling"
        ],
        "correctAnswer": 2,
        # "category": "security"
    },
    {
        "text": "What is the purpose of AWS CloudTrail?",
        "answers": [
            "To track API activity and user actions across AWS services",
            "To monitor network traffic",
            "To calculate costs and estimate AWS service usage",
            "To configure DNS settings for applications"
        ],
        "correctAnswer": 0,
        # "category": "monitoring and analytics"
    },
    {
        "text": "Which AWS service is primarily used for providing serverless computing without needing to manage servers?",
        "answers": [
            "Amazon EC2",
            "AWS Lambda",
            "Amazon RDS",
            "Amazon S3"
        ],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which AWS service provides a content delivery network (CDN) to distribute static and dynamic web content?",
        "answers": [
            "Amazon S3",
            "Amazon CloudFront",
            "Amazon Route 53",
            "AWS WAF"
        ],
        "correctAnswer": 1,
        # "category": "networking"
    },
    {
        "text": "What is the purpose of the AWS Well-Architected Framework?",
        "answers": [
            "To design AWS services for maximum cost savings",
            "To help build secure, reliable, efficient, and cost-effective systems in the cloud",
            "To optimize EC2 instances for better performance",
            "To monitor AWS service usage and detect anomalies"
        ],
        "correctAnswer": 1,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "What is Amazon Elastic Kubernetes Service (EKS) primarily used for?",
        "answers": [
            "Managing Docker containers on AWS",
            "Running machine learning models",
            "Handling large-scale relational database workloads",
            "Storing and analyzing logs from EC2 instances"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "Which AWS service is used to automatically provision and manage a fleet of virtual machines to support containerized workloads?",
        "answers": [
            "Amazon ECS",
            "Amazon EKS",
            "AWS Lambda",
            "AWS Fargate"
        ],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which of the following AWS services is used for migrating on-premises databases to AWS?",
        "answers": [
            "AWS Database Migration Service (DMS)",
            "Amazon RDS",
            "Amazon DynamoDB",
            "Amazon Aurora"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which service allows you to manage multiple AWS accounts and apply policies to them?",
        "answers": [
            "AWS Identity and Access Management (IAM)",
            "AWS Organizations",
            "AWS Shield",
            "Amazon EC2"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which of the following is a key feature of Amazon DynamoDB?",
        "answers": [
            "Supports only relational database structures",
            "Requires manual scaling for throughput capacity",
            "Automatically scales to accommodate increasing traffic",
            "Requires you to manage database backups manually"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "What is the maximum duration of the free usage tier for AWS Lambda invocations?",
        "answers": [
            "1 year",
            "5 years",
            "12 months",
            "Indefinite"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service offers data warehousing for big data analytics?",
        "answers": [
            "Amazon Aurora",
            "Amazon Redshift",
            "Amazon S3",
            "Amazon DynamoDB"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    }
]

QUESTIONS_10 = [
    {
        "text": "Which AWS service can be used to track and analyze your AWS spending patterns and resource usage?",
        "answers": [
            "AWS Billing and Cost Management Dashboard",
            "AWS CloudWatch",
            "AWS Trusted Advisor",
            "AWS CloudTrail"
        ],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "What is the primary benefit of using Spot Instances in AWS EC2?",
        "answers": [
            "Guaranteed availability at all times",
            "Lowest possible price compared to On-Demand and Reserved Instances",
            "Reserved capacity for a specific region",
            "Ability to scale up immediately without delay"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "What is a key feature of AWS Budgets?",
        "answers": [
            "It automatically optimizes EC2 instance usage for cost reduction",
            "It allows you to create custom alerts for cost and usage based on your defined threshold",
            "It provides detailed performance insights and recommendations",
            "It offers automatic scaling of AWS resources based on traffic"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which of the following is part of the AWS Cloud Adoption Framework (AWS CAF)?",
        "answers": [
            "People, Governance, Security, Operations, Platform, Business",
            "AWS Well-Architected Framework",
            "AWS Cost Explorer",
            "Amazon Aurora Database"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which migration strategy involves moving applications without changing the underlying code?",
        "answers": [
            "Rehosting (Lift and Shift)",
            "Replatforming",
            "Refactoring",
            "Retiring"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS service is primarily used for migrating large amounts of on-premises data to AWS using physical devices?",
        "answers": [
            "AWS Snowcone",
            "Amazon S3",
            "AWS DataSync",
            "AWS Direct Connect"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "What is the purpose of the AWS Marketplace?",
        "answers": [
            "To help AWS customers buy and sell software solutions that are integrated with AWS",
            "To manage and monitor AWS billing and cost management",
            "To automate the provisioning of EC2 instances",
            "To manage your AWS accounts and users"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "What is one key component of AWS’s sustainability efforts?",
        "answers": [
            "AWS resources are powered by 100% renewable energy",
            "AWS charges customers for unused resources to encourage efficiency",
            "AWS data centers are located exclusively in environmentally friendly countries",
            "AWS services are designed to use 20% less energy per instance"
        ],
        "correctAnswer": 0,
        # "category": "sustainability"
    },
    {
        "text": "Which of the following statements best describes Auto Scaling in AWS?",
        "answers": [
            "Automatically adjusts the number of EC2 instances based on user demand",
            "Automates the provisioning of storage volumes",
            "Improves security by scaling resources based on threat levels",
            "Automatically adjusts your application code based on traffic patterns"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "How does Amazon EC2 Auto Scaling ensure the availability of your application?",
        "answers": [
            "By automatically scaling the number of instances based on defined policies",
            "By distributing application traffic between multiple availability zones",
            "By selecting the lowest-cost EC2 instance type",
            "By enabling elastic IP addresses for each instance"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    }
]

QUESTIONS_11 = [
    {
        "text": "How does AWS ensure high availability for applications running in multiple Availability Zones?",
        "answers": [
            "By replicating all data across multiple regions",
            "By distributing instances and data across multiple Availability Zones within a region",
            "By scaling EC2 instances automatically based on traffic",
            "By providing load balancing at the edge locations"
        ],
        "correctAnswer": 1,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "What is a key feature of Amazon EC2 Auto Scaling?",
        "answers": [
            "It helps maintain performance and availability by automatically increasing or decreasing the number of EC2 instances based on demand",
            "It provides automatic backups of EC2 instances to multiple regions",
            "It provides automatic patching and updates for EC2 instances",
            "It monitors EC2 instances for security vulnerabilities"
        ],
        "correctAnswer": 0,
        # "category": "infrastructure and reliability"
    },
    {
        "text": "Which AWS service can be used to deploy applications without managing the underlying infrastructure?",
        "answers": [
            "AWS Elastic Beanstalk",
            "Amazon EC2",
            "AWS Lambda",
            "AWS CloudFormation"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "Which of the following AWS services is a serverless computing service?",
        "answers": [
            "Amazon EC2",
            "AWS Lambda",
            "Amazon Elastic Beanstalk",
            "Amazon RDS"
        ],
        "correctAnswer": 1,
        # "category": "compute"
    },
    {
        "text": "Which AWS service is used to monitor network traffic for malicious activity and unauthorized behavior?",
        "answers": [
            "Amazon GuardDuty",
            "AWS Shield",
            "AWS WAF",
            "Amazon CloudWatch"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "Which of the following best describes Amazon Glacier?",
        "answers": [
            "A fully managed NoSQL database service",
            "A low-cost storage service designed for data archiving and long-term backup",
            "A high-performance computing service for real-time data processing",
            "A CDN that distributes content to end users"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What type of AWS architecture allows for an application to automatically adjust its resources based on the load?",
        "answers": [
            "Auto Scaling",
            "Elastic Load Balancing",
            "Elastic File System",
            "AWS Lambda"
        ],
        "correctAnswer": 0,
        # "category": "compute"
    },
    {
        "text": "Which AWS service provides compliance certifications and attestation reports for AWS services and regions?",
        "answers": [
            "AWS Artifact",
            "AWS IAM",
            "AWS Shield",
            "Amazon CloudTrail"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "Which service would you use to track the history of AWS API calls and access to your resources?",
        "answers": [
            "Amazon CloudWatch",
            "AWS CloudTrail",
            "AWS GuardDuty",
            "AWS Config"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service would be most appropriate for a web application that requires high-performance object storage?",
        "answers": [
            "Amazon S3",
            "Amazon EFS",
            "Amazon EBS",
            "Amazon Glacier"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    }
]

QUESTIONS_12 = [
    {
        "text": "How does Amazon Aurora maintain high availability and durability for data?",
        "answers": [
            "By replicating six copies of data across three Availability Zones and continuously backing up to Amazon S3",
            "By automatically creating read replicas in different regions",
            "By creating a single backup in one Availability Zone",
            "By using an on-premises backup solution"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "What level of automatic backup does Amazon RDS provide?",
        "answers": [
            "RDS does not offer automatic backups",
            "RDS provides automatic backups of databases without user intervention",
            "Backups are only available with manual setup",
            "Backups require additional configuration using Amazon S3"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which service offers 1 million requests per month and 3.2 million seconds of compute time under the AWS Free Tier?",
        "answers": [
            "Amazon EC2",
            "AWS Lambda",
            "Amazon S3",
            "Amazon RDS"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "What is the storage limit for DynamoDB under the AWS Free Tier?",
        "answers": [
            "10 GB per month",
            "25 GB per month",
            "50 GB per month",
            "Unlimited storage"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS Cloud Adoption Framework (CAF) perspective focuses on training, role definition, and building a cloud culture?",
        "answers": [
            "Business",
            "People",
            "Governance",
            "Operations"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "What does the Platform perspective in the AWS Cloud Adoption Framework (CAF) focus on?",
        "answers": [
            "Cloud infrastructure, architecture, core services, and scalability",
            "User access policies and IAM",
            "Developing cloud financial models",
            "Building cloud-ready teams"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which pillar of the Well-Architected Framework is focused on protecting data and systems?",
        "answers": [
            "Cost Optimization",
            "Performance Efficiency",
            "Operational Excellence",
            "Security"
        ],
        "correctAnswer": 3,
        # "category": "security"
    },
    {
        "text": "What storage capacity does the AWS Snowcone device offer?",
        "answers": [
            "100 PB",
            "80 TB",
            "14 TB",
            "1 TB"
        ],
        "correctAnswer": 2,
        # "category": "migration and innovation"
    },
    {
        "text": "How much data can an AWS Snowmobile store?",
        "answers": [
            "1 TB",
            "14 TB",
            "80 TB",
            "100 PB"
        ],
        "correctAnswer": 3,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS Support Plan offers 24-hour email access for non-critical issues with a 12-hour response time for system impairments?",
        "answers": [
            "Basic",
            "Developer",
            "Business",
            "Enterprise On-Ramp"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "What level of support is available under the AWS Basic Support plan?",
        "answers": [
            "24/7 technical support with a 1-hour response time",
            "Access to whitepapers, documentation, and Trusted Advisor's basic features",
            "24-hour email access to AWS engineers",
            "Access to a designated Technical Account Manager"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS support plan provides a response time of 15 minutes for business-critical issues?",
        "answers": [
            "Developer",
            "Business",
            "Enterprise On-Ramp",
            "Enterprise"
        ],
        "correctAnswer": 3,
        # "category": "pricing and support"
    },
    {
        "text": "Which S3 storage class provides the fastest retrieval times, similar to Standard storage?",
        "answers": [
            "Glacier Deep Archive",
            "Glacier Flexible Retrieval",
            "Glacier Instant Retrieval",
            "S3 Standard-IA"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "What is the expected retrieval time for data in the Glacier Deep Archive storage class?",
        "answers": [
            "Milliseconds",
            "1-2 minutes",
            "3-5 hours",
            "12-48 hours"
        ],
        "correctAnswer": 3,
        # "category": "storage and databases"
    },
    {
        "text": "How much can you save on EC2 costs by using Spot Instances compared to On-Demand Instances?",
        "answers": [
            "Up to 50%",
            "Up to 60%",
            "Up to 70%",
            "Up to 90%"
        ],
        "correctAnswer": 3,
        # "category": "pricing and support"
    },
    {
        "text": "What is the cost of data transfers within the same region between AWS services, such as S3?",
        "answers": [
            "Free for both data ingress and egress",
            "Free for data ingress but charged for egress",
            "Free for data ingress only",
            "Free for egress only"
        ],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service replicates data automatically across multiple Availability Zones to ensure durability?",
        "answers": [
            "Amazon DynamoDB",
            "Amazon S3",
            "Amazon Redshift",
            "Amazon EC2"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What AWS support plan offers access to a pool of Technical Account Managers and a 30-minute response time for business-critical issues?",
        "answers": [
            "Developer",
            "Business",
            "Enterprise On-Ramp",
            "Enterprise"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "What service provides continuous backup and replication of data across multiple Availability Zones within a region?",
        "answers": [
            "Amazon EBS",
            "Amazon S3",
            "Amazon DynamoDB",
            "Amazon Redshift"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS service offers up to 25 GB of storage per month under the AWS Free Tier?",
        "answers": [
            "Amazon RDS",
            "Amazon EFS",
            "Amazon DynamoDB",
            "Amazon EC2"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    }
]

QUESTIONS_13 = [
    {
        "text": "What does the AWS Business Support Plan include in terms of response time for impaired production systems?",
        "answers": [
            "15 minutes for business-critical issues",
            "4 hours for impaired production systems and 1 hour for down production systems",
            "24 hours for any production system issue",
            "Immediate access to a Technical Account Manager"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS Free Tier option is available only for the first 12 months of usage?",
        "answers": [
            "Amazon DynamoDB storage",
            "AWS Lambda requests",
            "S3 Standard Storage",
            "CloudFront data transfer out"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "What is the primary focus of the Governance perspective within the AWS Cloud Adoption Framework (CAF)?",
        "answers": [
            "Ensuring business objectives align with cloud strategy",
            "Policies, compliance, access management, and monitoring",
            "Optimizing financials for cloud migration",
            "Defining roles and managing change"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Which perspective in the AWS Cloud Adoption Framework (CAF) focuses on risk management and compliance?",
        "answers": [
            "Security",
            "Operations",
            "Platform",
            "Governance"
        ],
        "correctAnswer": 3,
        # "category": "migration and innovation"
    },
    {
        "text": "What AWS Well-Architected pillar is concerned with minimizing operational costs and improving resource utilization?",
        "answers": [
            "Security",
            "Cost Optimization",
            "Operational Excellence",
            "Sustainability"
        ],
        "correctAnswer": 1,
        # "category": "security"
    },
    {
        "text": "Which AWS service allows data retrieval from 1 minute to 12 hours and is less expensive than Glacier Instant Retrieval?",
        "answers": [
            "S3 Standard",
            "S3 Glacier Flexible Retrieval",
            "S3 Intelligent-Tiering",
            "S3 Glacier Deep Archive"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Under which AWS Support Plan do users gain access to Concierge support for billing and account assistance?",
        "answers": [
            "Basic",
            "Developer",
            "Business",
            "Enterprise On-Ramp"
        ],
        "correctAnswer": 3,
        # "category": "pricing and support"
    },
    {
        "text": "What is the designated retrieval time for data stored in Amazon S3 Glacier Deep Archive?",
        "answers": [
            "Milliseconds",
            "1-2 minutes",
            "12-48 hours",
            "3-5 days"
        ],
        "correctAnswer": 2,
        # "category": "storage and databases"
    },
    {
        "text": "How does Amazon DynamoDB achieve high availability and reliability?",
        "answers": [
            "By replicating data across multiple regions by default",
            "By replicating data across multiple Availability Zones within a region",
            "By relying on user-defined replication configurations",
            "By using Amazon S3 for data backups"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS Cloud Adoption Framework (CAF) perspective focuses on financials, business cases, and aligning cloud usage with business goals?",
        "answers": [
            "Governance",
            "Operations",
            "Business",
            "Security"
        ],
        "correctAnswer": 2,
        # "category": "migration and innovation"
    },
    {
        "text": "In the AWS Well-Architected Framework, which pillar focuses on building systems that can recover from failures?",
        "answers": [
            "Reliability",
            "Operational Excellence",
            "Cost Optimization",
            "Security"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "How does the AWS Enterprise Support Plan differ from the Enterprise On-Ramp Support Plan?",
        "answers": [
            "Enterprise Support has a 15-minute response time for business-critical issues and a designated Technical Account Manager",
            "Enterprise On-Ramp includes 24/7 phone support while Enterprise Support does not",
            "Enterprise Support is free for the first 12 months",
            "Enterprise On-Ramp offers faster response times than Enterprise Support"
        ],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service offers a free data transfer in the same region between services?",
        "answers": [
            "Amazon CloudFront",
            "Amazon EC2",
            "Amazon S3",
            "AWS Snowball"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "What AWS service allows up to 80 TB of data transfer on a single device for physical data migration?",
        "answers": [
            "Snowcone",
            "Snowball",
            "Snowmobile",
            "Direct Connect"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS Snow Family member provides 100 petabytes of storage for data migration?",
        "answers": [
            "Snowcone",
            "Snowball",
            "Snowmobile",
            "Snowcart"
        ],
        "correctAnswer": 2,
        # "category": "migration and innovation"
    },
    {
        "text": "What does the Operations perspective in the AWS CAF focus on?",
        "answers": [
            "Performance monitoring, incident management, and operational efficiency",
            "Cloud architecture development and data storage",
            "Governance and compliance strategies",
            "Role definition and workforce development"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "What is the main benefit of using Spot Instances in AWS EC2?",
        "answers": [
            "High availability",
            "Lower costs, with savings up to 90%",
            "Predictable performance",
            "Increased security"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "How does Amazon S3 Glacier Instant Retrieval differ from Glacier Deep Archive?",
        "answers": [
            "Instant Retrieval offers access in milliseconds, while Deep Archive takes up to 48 hours",
            "Deep Archive is faster but more expensive than Instant Retrieval",
            "Deep Archive is available for 12 months free under AWS Free Tier",
            "Instant Retrieval has a lower durability than Deep Archive"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "Which AWS support plan provides unrestricted technical support cases and is best for developing solutions on AWS?",
        "answers": [
            "Basic",
            "Developer",
            "Business",
            "Enterprise On-Ramp"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "What AWS service provides access management and policy control features for cloud security?",
        "answers": [
            "Amazon S3",
            "Amazon RDS",
            "IAM (Identity and Access Management)",
            "AWS Lambda"
        ],
        "correctAnswer": 2,
        # "category": "security"
    }
]

QUESTIONS_14 = [
    {
        "text": "What is the data storage limit for Amazon DynamoDB under the Always Free Tier?",
        "answers": [
            "1 GB",
            "10 GB",
            "25 GB",
            "50 GB"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "In the AWS Well-Architected Framework, which pillar is primarily concerned with energy efficiency and reducing environmental impact?",
        "answers": [
            "Operational Excellence",
            "Security",
            "Reliability",
            "Sustainability"
        ],
        "correctAnswer": 3,
        # "category": "security"
    },
    {
        "text": "Which AWS service provides six copies of data across three Availability Zones?",
        "answers": [
            "Amazon RDS",
            "Amazon Aurora",
            "Amazon DynamoDB",
            "Amazon S3"
        ],
        "correctAnswer": 1,
        # "category": "storage and databases"
    },
    {
        "text": "What is the response time for the AWS Enterprise Support Plan for business-critical issues?",
        "answers": [
            "24 hours",
            "12 hours",
            "1 hour",
            "15 minutes"
        ],
        "correctAnswer": 3,
        # "category": "pricing and support"
    },
    {
        "text": "What storage capacity is available with AWS Snowcone?",
        "answers": [
            "10 TB",
            "14 TB",
            "80 TB",
            "100 PB"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS CAF perspective would focus on training, change management, and role definition?",
        "answers": [
            "Business",
            "People",
            "Governance",
            "Operations"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS service includes a 12-month free tier for a specified amount of standard storage?",
        "answers": [
            "AWS Lambda",
            "Amazon EC2",
            "Amazon S3",
            "Amazon RDS"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "Which pillar of the AWS Well-Architected Framework focuses on automation of operational procedures to improve efficiency?",
        "answers": [
            "Operational Excellence",
            "Performance Efficiency",
            "Reliability",
            "Cost Optimization"
        ],
        "correctAnswer": 0,
        # "category": "security"
    },
    {
        "text": "Which AWS support plan provides unrestricted email technical support with response times under 12 hours for impaired systems?",
        "answers": [
            "Developer",
            "Business",
            "Enterprise",
            "Basic"
        ],
        "correctAnswer": 0,
        # "category": "pricing and support"
    },
    {
        "text": "What is the primary focus of the Platform perspective in the AWS CAF?",
        "answers": [
            "Incident response and operational management",
            "Cloud infrastructure, architecture, and scalability",
            "Business alignment and financial goals",
            "IAM policies and data security"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "Which Amazon S3 storage tier provides the lowest-cost option for infrequent access with retrieval times of 12-48 hours?",
        "answers": [
            "S3 Standard",
            "S3 Glacier Instant Retrieval",
            "S3 Glacier Flexible Retrieval",
            "S3 Glacier Deep Archive"
        ],
        "correctAnswer": 3,
        # "category": "storage and databases"
    },
    {
        "text": "Under the AWS Free Tier, how many Lambda requests per month are free?",
        "answers": [
            "100,000",
            "500,000",
            "1 million",
            "2 million"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    },
    {
        "text": "Which CAF perspective deals with aligning cloud strategy with KPIs and financials?",
        "answers": [
            "Business",
            "People",
            "Platform",
            "Security"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "How long does AWS automatically back up data in Amazon RDS by default?",
        "answers": [
            "7 days",
            "14 days",
            "30 days",
            "60 days"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "What support plan should you choose if you need direct phone access to AWS support with a 4-hour response time for production system issues?",
        "answers": [
            "Developer",
            "Business",
            "Enterprise On-Ramp",
            "Basic"
        ],
        "correctAnswer": 1,
        # "category": "pricing and support"
    },
    {
        "text": "Which AWS service automatically replicates data across Availability Zones to improve durability?",
        "answers": [
            "Amazon Aurora",
            "Amazon CloudFront",
            "Amazon EC2",
            "AWS IAM"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "What is the primary focus of the Operations perspective in the AWS CAF?",
        "answers": [
            "Incident and event management, backups, and performance monitoring",
            "Defining business objectives and aligning cloud strategy",
            "Policies and compliance management",
            "Training and change management"
        ],
        "correctAnswer": 0,
        # "category": "migration and innovation"
    },
    {
        "text": "Which AWS Snow Family device can store up to 100 petabytes for data transfer?",
        "answers": [
            "Snowcone",
            "Snowmobile",
            "Snowball",
            "Glacier Deep Archive"
        ],
        "correctAnswer": 1,
        # "category": "migration and innovation"
    },
    {
        "text": "How does Amazon Aurora maintain high availability of data?",
        "answers": [
            "By storing six copies across three Availability Zones",
            "By using a single Availability Zone with automatic backups",
            "By relying on user-defined replication",
            "By using Amazon S3 as backup"
        ],
        "correctAnswer": 0,
        # "category": "storage and databases"
    },
    {
        "text": "Which support plan includes a pool of Technical Account Managers to provide additional guidance?",
        "answers": [
            "Developer",
            "Business",
            "Enterprise On-Ramp",
            "Basic"
        ],
        "correctAnswer": 2,
        # "category": "pricing and support"
    }
]

QUESTIONS_15 = [
    {
        "text": "In Amazon Aurora, how many copies of data are stored across Availability Zones, and where is data backed up continuously?",
        "answers": [
            "Four copies in two Availability Zones, backed up to Amazon RDS",
            "Six copies in three Availability Zones, backed up to Amazon S3",
            "Three copies in two Availability Zones, backed up to Amazon Glacier",
            "Nine copies in three Availability Zones, backed up to Amazon DynamoDB"
        ],
        "correctAnswer": 1
    },
    {
        "text": "Which AWS Well-Architected Framework pillar emphasizes automation of operational procedures to enhance efficiency and reduce manual intervention?",
        "answers": [
            "Reliability",
            "Performance Efficiency",
            "Operational Excellence",
            "Cost Optimization"
        ],
        "correctAnswer": 2
    },
    {
        "text": "In the AWS CAF Governance perspective, what specific practice is recommended to ensure secure access to cloud resources?",
        "answers": [
            "Implementation of cloud training programs",
            "Defining business objectives and KPIs",
            "Establishing IAM policies and using logging and monitoring",
            "Defining financial metrics and case studies"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which support plan offers access to the AWS Health API, Trusted Advisor checks, and has response times of under 1 hour for production system failures?",
        "answers": [
            "Basic",
            "Developer",
            "Business",
            "Enterprise On-Ramp"
        ],
        "correctAnswer": 3
    },
    {
        "text": "How does AWS Snowmobile securely transport data from client locations to AWS?",
        "answers": [
            "By replicating data across multiple regions during transit",
            "Through encrypted network connections only",
            "Using specialized vehicles with physical and network encryption",
            "Through portable encrypted SSDs delivered to AWS facilities"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which AWS Free Tier service includes 25 GB of storage per month for free?",
        "answers": [
            "Amazon RDS",
            "Amazon S3",
            "Amazon DynamoDB",
            "Amazon EC2"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which S3 storage tier is recommended for data that requires instant retrieval with minimal access frequency?",
        "answers": [
            "S3 Standard",
            "S3 Glacier Flexible Retrieval",
            "S3 Glacier Deep Archive",
            "S3 Glacier Instant Retrieval"
        ],
        "correctAnswer": 3
    },
    {
        "text": "What AWS CAF perspective is primarily responsible for aligning cloud initiatives with business strategy, goals, and KPIs?",
        "answers": [
            "Platform",
            "People",
            "Business",
            "Governance"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which of the following can enable up to 90% cost savings on Amazon EC2 instances?",
        "answers": [
            "Reserved Instances",
            "Spot Instances",
            "On-Demand Instances",
            "Dedicated Hosts"
        ],
        "correctAnswer": 1
    },
    {
        "text": "How does Amazon RDS provide automated backups for databases, and what is the default backup retention period?",
        "answers": [
            "By storing snapshots every 30 minutes; 14 days retention",
            "Using continuous backups stored on Amazon Glacier; 7 days retention",
            "By taking automatic daily snapshots; 7 days retention",
            "Using multi-AZ replication for high availability; 30 days retention"
        ],
        "correctAnswer": 2
    },
    {
        "text": "In the Well-Architected Framework, which pillar emphasizes optimization of workloads for consistent high performance under various demand levels?",
        "answers": [
            "Reliability",
            "Performance Efficiency",
            "Operational Excellence",
            "Cost Optimization"
        ],
        "correctAnswer": 1
    },
    {
        "text": "Which AWS service provides data replication across three Availability Zones to enhance durability?",
        "answers": [
            "Amazon EC2",
            "Amazon Aurora",
            "Amazon S3",
            "AWS Lambda"
        ],
        "correctAnswer": 1
    },
    {
        "text": "In AWS CAF, which perspective is focused on policies, access management, and risk assessment?",
        "answers": [
            "Governance",
            "Operations",
            "Platform",
            "People"
        ],
        "correctAnswer": 0
    },
    {
        "text": "Which support plan includes direct access to Technical Account Managers (TAMs) and a 15-minute response time for business-critical issues?",
        "answers": [
            "Developer",
            "Business",
            "Enterprise",
            "Enterprise On-Ramp"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which Snow Family device can handle data transfer needs up to 80 TB?",
        "answers": [
            "Snowcone",
            "Snowball",
            "Snowmobile",
            "AWS Storage Gateway"
        ],
        "correctAnswer": 1
    },
    {
        "text": "What are the recommended uses for Amazon S3 Glacier Deep Archive?",
        "answers": [
            "Frequent retrievals with low latency requirements",
            "Infrequent access with occasional retrieval needs",
            "Archival storage with retrieval times ranging from 12 to 48 hours",
            "Real-time analytics and data processing"
        ],
        "correctAnswer": 2
    },
    {
        "text": "What is the maximum response time for support requests under the Developer support plan?",
        "answers": [
            "1 hour",
            "12 hours",
            "24 hours",
            "48 hours"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which AWS service allows data to be transferred into AWS at no cost when staying within the same region?",
        "answers": [
            "Amazon EC2",
            "Amazon RDS",
            "AWS Lambda",
            "Amazon S3"
        ],
        "correctAnswer": 3
    },
    {
        "text": "Which AWS CAF perspective covers cloud culture, HR management, and team training aspects?",
        "answers": [
            "People",
            "Business",
            "Operations",
            "Security"
        ],
        "correctAnswer": 0
    },
    {
        "text": "For which of the following scenarios is the AWS S3 Glacier Flexible Retrieval option best suited?",
        "answers": [
            "Data required for real-time analytics",
            "Data needed in milliseconds",
            "Data required with retrieval times between 1 minute and 12 hours",
            "Data access limited to once per month"
        ],
        "correctAnswer": 2
    },
    {
        "text": "How does Amazon DynamoDB ensure durability and availability across multiple regions?",
        "answers": [
            "Through multi-AZ replication",
            "By continuous snapshots to Amazon S3",
            "Using point-in-time recovery with Amazon RDS",
            "By default replication across three regions"
        ],
        "correctAnswer": 0
    },
    {
        "text": "In AWS's shared responsibility model, what is AWS responsible for when managing Amazon S3 data?",
        "answers": [
            "Configuring access control lists (ACLs)",
            "Encrypting data upon upload",
            "Infrastructure security of storage hardware",
            "Data classification and compliance"
        ],
        "correctAnswer": 2
    },
    {
        "text": "What response time is guaranteed for business-critical issues under the AWS Enterprise On-Ramp support plan?",
        "answers": [
            "1 hour",
            "30 minutes",
            "15 minutes",
            "4 hours"
        ],
        "correctAnswer": 1
    },
    {
        "text": "Which AWS Snow Family device is designed for data migrations of up to 14 TB with rugged portability?",
        "answers": [
            "Snowcone",
            "Snowball",
            "Snowmobile",
            "AWS Storage Gateway"
        ],
        "correctAnswer": 0
    },
    {
        "text": "What is a key characteristic of Spot Instances that differentiates them from Reserved Instances?",
        "answers": [
            "They are available at a fixed cost",
            "They can be terminated by AWS if capacity is required",
            "They are reserved for 1-3 years",
            "They have access to all instance types"
        ],
        "correctAnswer": 1
    },
    {
        "text": "In the AWS Well-Architected Framework, which pillar focuses on protecting workloads through encryption, threat detection, and IAM?",
        "answers": [
            "Operational Excellence",
            "Security",
            "Reliability",
            "Performance Efficiency"
        ],
        "correctAnswer": 1
    },
    {
        "text": "What AWS support level includes Concierge support for billing and account assistance?",
        "answers": [
            "Basic",
            "Developer",
            "Enterprise",
            "Business"
        ],
        "correctAnswer": 2
    },
    {
        "text": "Which AWS CAF perspective is responsible for incident and event management as part of cloud operations?",
        "answers": [
            "Operations",
            "Platform",
            "Security",
            "Governance"
        ],
        "correctAnswer": 0
    },
    {
        "text": "Which Amazon S3 storage tier offers instant access and is cost-effective for data accessed infrequently?",
        "answers": [
            "S3 Standard-IA",
            "S3 Glacier Deep Archive",
            "S3 One Zone-IA",
            "S3 Glacier Flexible Retrieval"
        ],
        "correctAnswer": 0
    },
    {
        "text": "What AWS service provides up to 3.2 million seconds of compute time per month under the Always Free Tier?",
        "answers": [
            "Amazon EC2",
            "AWS Lambda",
            "Amazon RDS",
            "Amazon S3"
        ],
        "correctAnswer": 1
    }
]

QUESTIONS_16 = [
    {
        "text": "Which Aurora feature enhances durability by storing six copies of data across multiple Availability Zones?",
        "answers": [
            "Data replication across multiple regions",
            "Six copies of data across three Availability Zones",
            "Automatic scaling across zones",
            "Serverless scaling"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "Under which AWS support plan do you have access to all AWS Trusted Advisor checks and receive a 4-hour response time for production system impairments?",
        "answers": [
            "Basic",
            "Developer",
            "Business",
            "Enterprise"
        ],
        "correctAnswer": 2,
    },
    {
        "text": "How does Amazon S3 ensure the high durability of stored data across regions and zones, particularly with Glacier storage classes?",
        "answers": [
            "Replicates data across availability zones",
            "Data is replicated between regions",
            "Data is encrypted and compressed before storage",
            "Data is replicated across regions every 24 hours"
        ],
        "correctAnswer": 0,
    },
    {
        "text": "Which AWS CAF perspective is specifically concerned with training, change management, and defining roles to support cloud migration?",
        "answers": [
            "Business",
            "People",
            "Security",
            "Platform"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "Which service is ideal for quickly transferring large volumes of data to AWS when local internet bandwidth is limited, and requires up to 100 PB storage capacity?",
        "answers": [
            "AWS Snowcone",
            "AWS Snowball",
            "AWS Snowmobile",
            "AWS Direct Connect"
        ],
        "correctAnswer": 2,
    },
    {
        "text": "What is the maximum response time for business-critical issues under the AWS Enterprise support plan?",
        "answers": [
            "1 hour",
            "30 minutes",
            "15 minutes",
            "4 hours"
        ],
        "correctAnswer": 2,
    },
    {
        "text": "What type of storage is recommended for data with unpredictable retrieval requirements but requires milliseconds-level access?",
        "answers": [
            "S3 Standard",
            "S3 Glacier Instant Retrieval",
            "EBS Volume",
            "RDS"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "In AWS’s shared responsibility model, which of the following is an AWS responsibility for Amazon S3?",
        "answers": [
            "Managing encryption of data at rest",
            "Managing encryption of data in transit",
            "Managing access control policies",
            "All of the above"
        ],
        "correctAnswer": 0,
    },
    {
        "text": "Which of the following is free under the AWS Free Tier for 12 months but has specific storage limitations?",
        "answers": [
            "S3 Standard storage",
            "Lambda",
            "EC2 instances",
            "CloudFront data transfer out"
        ],
        "correctAnswer": 0,
    },
    {
        "text": "Which AWS Well-Architected pillar is focused on maintaining the ability of workloads to recover from infrastructure or service failures?",
        "answers": [
            "Reliability",
            "Performance Efficiency",
            "Security",
            "Cost Optimization"
        ],
        "correctAnswer": 0,
    },
    {
        "text": "What is the primary use of AWS Cost Explorer?",
        "answers": [
            "Monitor application performance",
            "Create cost reports and forecasts",
            "Optimize cloud architecture",
            "Automate backup processes"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "Which of the following does AWS Trusted Advisor NOT provide checks for?",
        "answers": [
            "Security",
            "Performance",
            "Fault tolerance",
            "Identity and access management"
        ],
        "correctAnswer": 3,
    },
    {
        "text": "What is the response time provided by AWS Developer Support for general inquiries?",
        "answers": [
            "1 hour",
            "12 hours",
            "24 hours",
            "48 hours"
        ],
        "correctAnswer": 2,
    },
    {
        "text": "In the AWS CAF, which perspective addresses the alignment of cloud strategies with business objectives and financial management?",
        "answers": [
            "Business",
            "People",
            "Governance",
            "Operations"
        ],
        "correctAnswer": 0,
    },
    {
        "text": "Which AWS service offers block-level storage for EC2 instances and provides snapshots for backup?",
        "answers": [
            "S3",
            "EBS",
            "EFS",
            "Glacier"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "Which AWS pricing model offers the ability to save up to 90% on EC2 costs?",
        "answers": [
            "On-demand instances",
            "Reserved instances",
            "Spot instances",
            "Savings plans"
        ],
        "correctAnswer": 2,
    },
    {
        "text": "Which of the following storage classes in S3 provides the cheapest option but has an access time of 12-48 hours?",
        "answers": [
            "Standard",
            "Intelligent-Tiering",
            "Glacier Deep Archive",
            "S3 One Zone-IA"
        ],
        "correctAnswer": 2,
    },
    {
        "text": "Which AWS service automatically provides backups for relational databases?",
        "answers": [
            "Amazon S3",
            "Amazon RDS",
            "AWS Backup",
            "Amazon Aurora"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "Which AWS service allows you to store and manage Docker images?",
        "answers": [
            "Amazon S3",
            "Amazon ECS",
            "AWS Lambda",
            "Amazon ECR"
        ],
        "correctAnswer": 3,
    },
    {
        "text": "What AWS service enables automatic scaling of applications without provisioning or managing servers?",
        "answers": [
            "AWS Lambda",
            "Amazon ECS",
            "AWS Elastic Beanstalk",
            "AWS Fargate"
        ],
        "correctAnswer": 0,
    },
    {
        "text": "Which AWS service is used for real-time data processing and management of NoSQL databases?",
        "answers": [
            "Amazon RDS",
            "Amazon DynamoDB",
            "Amazon Redshift",
            "Amazon S3"
        ],
        "correctAnswer": 1,
    },
    {
        "text": "Which of the following AWS services provides a managed environment for running Kubernetes clusters?",
        "answers": [
            "Amazon ECS",
            "Amazon EKS",
            "Amazon Fargate",
            "Amazon Lambda"
        ],
        "correctAnswer": 1,
    },
]
