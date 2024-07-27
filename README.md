# Resource Library
Headstarter Hackathon Project: Community-driven library of resources with search & filter features,
with API integration for authentication of user-uploaded resources.

## Project Setup:
### Project Structure:
- **Setup:** git clone repository in local environment
- **Install dependencies:** pip install -r backend/requirements.txt
### MongoDB:
- **Accept invite** from MongoDB Atlas project
- **Create User:** Database Access->Add New Database User->create username/password + set built-in role to Atlas Admin.
- **Connect to Database:** All Clusters->ResourceLibraryCluster->Connect->follow instructions to setup shared Database locally.
- **Setup Environment Variables:**  Create .env (if not already, add to .gitignore), set MONGO_URI=your-mongodb-connection-string
- **Recommnedation:** Use MongoDB Compass for visualizing database structure

## TODO List:
- [x] Setup Initial Project Structure.
- [x] Connect MongoDB database.
- [ ] Frontend of site - Resource Library layout
- [ ] Frontend search bar + add resource button + upload resource modal form
- [ ] JS integration (onclick, onsubmit, etc.,)
- [ ] Backend logic + storing resources in database on submit of resource form
- [ ] AI Summary Feature
- [ ] Test and Refine website
- [ ] Google Analytics and get users
- [ ] Create presentation and video demo for submission
